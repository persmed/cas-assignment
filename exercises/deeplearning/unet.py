from collections import OrderedDict
import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
#
class ContractingBlock(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size=3, short_skip=True, broadcast=False):
        super(ContractingBlock, self).__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.short_skip = short_skip
        self.broadcast = broadcast

        self.conv2d_1 = torch.nn.Conv2d(kernel_size=kernel_size, in_channels=in_channels, out_channels=out_channels, padding=1)
        self.bn_1 = torch.nn.BatchNorm2d(out_channels)
        self.conv2d_2 = torch.nn.Conv2d(kernel_size=kernel_size, in_channels=out_channels, out_channels=out_channels, padding=1)
        self.bn_2 = torch.nn.BatchNorm2d(out_channels)

    def forward(self, input):
        x_conv2d = self.conv2d_1(input)
        x = F.relu(x_conv2d , inplace=False)
        x = self.bn_1(x)
        x = self.conv2d_2(x)
        x = F.relu(x , inplace=False)
        x = self.bn_2(x)

        if self.short_skip:
            x = torch.add(x, x_conv2d)
        elif self.broadcast:
            x = torch.add(x, input)

class UNet(nn.Module):
    def contracting_block(self, in_channels, out_channels, kernel_size=3):
        block = torch.nn.Sequential(OrderedDict([
                    ('conv1', torch.nn.Conv2d(kernel_size=kernel_size, in_channels=in_channels, out_channels=out_channels, padding=1)),
                    ('relu1', torch.nn.ReLU()),
                    ('bn1', torch.nn.BatchNorm2d(out_channels)),
                    ('conv2', torch.nn.Conv2d(kernel_size=kernel_size, in_channels=out_channels, out_channels=out_channels, padding=1)),
                    ('relu2', torch.nn.ReLU()),
                    ('bn2', torch.nn.BatchNorm2d(out_channels))])
                )
        return block

    def expansive_block(self, in_channels, mid_channel, out_channels, kernel_size=3, p_dropout=0.5):
            block = torch.nn.Sequential(
                    torch.nn.Dropout2d(p=p_dropout),
                    torch.nn.Conv2d(kernel_size=kernel_size, in_channels=in_channels, out_channels=mid_channel, padding=1),
                    torch.nn.ReLU(),
                    torch.nn.BatchNorm2d(mid_channel),
                    torch.nn.Dropout2d(p=p_dropout),
                    torch.nn.Conv2d(kernel_size=kernel_size, in_channels=mid_channel, out_channels=mid_channel, padding=1),
                    torch.nn.ReLU(),
                    torch.nn.BatchNorm2d(mid_channel),
                    torch.nn.ConvTranspose2d(in_channels=mid_channel, out_channels=out_channels, kernel_size=3, stride=2, padding=1, output_padding=1)
                    )
            return  block

    def final_block(self, in_channels, mid_channel, out_channels, kernel_size=3, p_dropout=0.5):
            block = torch.nn.Sequential(
                    torch.nn.Dropout2d(p=p_dropout),
                    torch.nn.Conv2d(kernel_size=kernel_size, in_channels=in_channels, out_channels=mid_channel, padding=1),
                    torch.nn.ReLU(),
                    torch.nn.BatchNorm2d(mid_channel),
                    torch.nn.Dropout2d(p=p_dropout),
                    torch.nn.Conv2d(kernel_size=kernel_size, in_channels=mid_channel, out_channels=mid_channel, padding=1),
                    torch.nn.ReLU(),
                    torch.nn.BatchNorm2d(mid_channel),
                    torch.nn.Conv2d(kernel_size=kernel_size, in_channels=mid_channel, out_channels=out_channels, padding=1),
                    torch.nn.ReLU(),
                    torch.nn.BatchNorm2d(out_channels),
                    )
            return  block

    def __init__(self, in_channel, out_channel):
        super(UNet, self).__init__()
        #Encode
        self.conv_encode1 = self.contracting_block(in_channels=in_channel, out_channels=64)#, short_skip=False, broadcast=True)
        self.conv_maxpool1 = torch.nn.MaxPool2d(kernel_size=2)
        self.conv_encode2 = self.contracting_block(64, 128)
        self.conv_maxpool2 = torch.nn.MaxPool2d(kernel_size=2)
        self.conv_encode3 = self.contracting_block(128, 256)
        self.conv_maxpool3 = torch.nn.MaxPool2d(kernel_size=2)
        # Bottleneck
        self.bottleneck = torch.nn.Sequential(
                            torch.nn.Conv2d(kernel_size=3, in_channels=256, out_channels=512, padding=1),
                            torch.nn.ReLU(),
                            torch.nn.BatchNorm2d(512),
                            torch.nn.Conv2d(kernel_size=3, in_channels=512, out_channels=512, padding=1),
                            torch.nn.ReLU(),
                            torch.nn.BatchNorm2d(512),
                            torch.nn.ConvTranspose2d(in_channels=512, out_channels=256, kernel_size=3, stride=2, padding=1, output_padding=1)
                            )
        # Decode
        self.conv_decode3 = self.expansive_block(512, 256, 128)
        self.conv_decode2 = self.expansive_block(256, 128, 64)
        self.final_layer = self.final_block(128, 64, out_channel)

    def crop_and_concat(self, upsampled, bypass, crop=False):
        if crop:
            c = (bypass.size()[2] - upsampled.size()[2]) // 2
            bypass = F.pad(bypass, (-c, -c, -c, -c))
        return torch.cat((upsampled, bypass), 1)

    def forward(self, x):
        # Encode
        encode_block1 = self.conv_encode1(x)
        encode_block1 = torch.add(encode_block1, x)
        encode_pool1 = self.conv_maxpool1(encode_block1)

        encode_block2 = self.conv_encode2(encode_pool1)
        # print(self.conv_encode2[0])
        # print(encode_block2['conv1'])
        # encode_block2 = torch.add(encode_block2, encode_pool1)
        encode_pool2 = self.conv_maxpool2(encode_block2)

        encode_block3 = self.conv_encode3(encode_pool2)
        encode_pool3 = self.conv_maxpool3(encode_block3)
        # Bottleneck
        bottleneck1 = self.bottleneck(encode_pool3)
        # Decode

        decode_block3 = self.crop_and_concat(bottleneck1, encode_block3, crop=True)
        cat_layer2 = self.conv_decode3(decode_block3)
        decode_block2 = self.crop_and_concat(cat_layer2, encode_block2, crop=True)
        cat_layer1 = self.conv_decode2(decode_block2)
        decode_block1 = self.crop_and_concat(cat_layer1, encode_block1, crop=True)
        final_layer = self.final_layer(decode_block1)
        return  final_layer
