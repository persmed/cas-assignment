import torch
from torch.utils.data import DataLoader
from torchvision import transforms
import matplotlib.pyplot as plt
import unet
import numpy as np
import dataset
from PIL import Image
import nibabel as nib
from scipy import ndimage
import os
import csv
import json
from tqdm import tqdm
import collections
from evaluation import evaluate
import argparse
import csv

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def bbox2_3D(img):
    r = np.any(img, axis=(1, 2))
    c = np.any(img, axis=(0, 2))
    z = np.any(img, axis=(0, 1))

    rmin, rmax = np.where(r)[0][[0, -1]]
    cmin, cmax = np.where(c)[0][[0, -1]]
    zmin, zmax = np.where(z)[0][[0, -1]]

    return [rmin, rmax, cmin, cmax, zmin, zmax]

def keep_largest(predictions):
    predictions_labels, num_features = ndimage.measurements.label(predictions)
    unique, counts = np.unique(predictions_labels, return_counts=True)
    counts_dict = dict(zip(unique, counts))
    #
    counts_dict = sorted(counts_dict.items(), key=lambda kv: kv[1], reverse = True)
    counts_dict = collections.OrderedDict(counts_dict)

    for i, lbl in enumerate(counts_dict):
        if i < 2:
            continue
        predictions[predictions_labels == lbl] = 0
    return predictions

class TumorSegmenter:
    def __init__(self, device, weights, show_plots=False):
        num_class = 1
        self.model = unet.UNet(num_class, num_class).to(device)
        self.model.load_state_dict(torch.load(weights, map_location=torch.device(device)))
        self.model.eval()
        self.show_plots = show_plots

    def segment(self, volume, liver_mask):
        trans = transforms.Compose([
                    # transforms.Resize((256, 256), interpolation=Image.LINEAR),
                    transforms.ToTensor()])
        trans2 = transforms.Compose([
                    transforms.ToPILImage()]),
                    # transforms.Resize((512, 512), interpolation=Image.NEAREST)])
        input = volume.get_fdata().astype(np.float32)
        # liver_mask = liver_segmentation.get_fdata().astype(np.uint8)

        liver_mask_cp = ndimage.binary_dilation(liver_mask).astype(np.uint8)

        for i in range(5):
            liver_mask_cp = ndimage.binary_dilation(liver_mask_cp)
        input[liver_mask_cp == 0] = 0
        bbox = bbox2_3D(liver_mask_cp)
        # input = np.clip(input, -100, 200)

        input = np.rot90(input).copy()
        input = np.transpose(input, (2, 0, 1))
        predictions = np.zeros(input.shape)

        slices = input.shape[0]

        if self.show_plots:
            plt.figure(1)

        pbar = tqdm(total = bbox[5] - bbox[4])

        for slice_nr in range(bbox[4], bbox[5]):
            slice_cpu = input[slice_nr, :, :]
            slice_cpu = Image.fromarray(slice_cpu)

            output = None

            slice = trans(slice_cpu)
            slice = slice.unsqueeze(1)
            slice = slice.to(device)
            output = self.model(slice)

            output = torch.sigmoid(output).data.cpu().numpy()[0, :, :, :]
            output = output[0, :, :]
            output[output < 0.5] = 0
            output[output > 0] = 1

            output = ndimage.binary_fill_holes(output).astype(np.uint8)
            # output = ndimage.binary_dilation(output).astype(np.uint8)

            output = Image.fromarray(output)
            output = output.resize((predictions.shape[1], predictions.shape[2]), resample=Image.LINEAR)
            output = np.array(output)
            predictions[slice_nr, :, :] = output

            if self.show_plots:
                slice_cpu = slice_cpu.resize((predictions.shape[1], predictions.shape[2]), resample=Image.LINEAR)
                slice_cpu = np.array(slice_cpu)
                plt.clf()
                plt.figure(1)
                plt.imshow(slice_cpu, cmap='gray', interpolation=None)
                plt.imshow(output, cmap='jet', alpha=0.5, interpolation=None)
                plt.pause(0.0001)
            pbar.update(1)
        pbar.close()

        predictions = predictions.astype(np.uint8)
        predictions = np.transpose(predictions, (1, 2, 0))
        # predictions = ndimage.binary_opening(predictions).astype(np.uint8)

        for i in range(3):
            predictions = np.rot90(predictions).copy()

        predictions[liver_mask == 0] = 0

        return predictions

class LiverSegmenter:
    def __init__(self, device, weights, show_plots=False):
        num_class = 1
        self.model = unet.UNet(num_class, num_class).to(device)
        self.model.load_state_dict(torch.load(weights, map_location=torch.device(device)))
        self.model.eval()
        self.show_plots = show_plots

    def segment(self, volume):
        trans = transforms.Compose([
                    transforms.Resize((256, 256), interpolation=Image.LINEAR),
                    transforms.ToTensor()])
        trans2 = transforms.Compose([
                    transforms.ToPILImage(),
                    transforms.Resize((512, 512), interpolation=Image.NEAREST)])
        input = volume.get_fdata().astype(np.float32)
        # input = np.clip(input, -100, 200)

        input = np.rot90(input).copy()
        input = np.transpose(input, (2, 0, 1))
        predictions = np.zeros(input.shape)

        slices = input.shape[0]

        if self.show_plots:
            plt.figure(1)

        pbar = tqdm(total = slices)

        for slice_nr in range(slices):
            slice_cpu = input[slice_nr, :, :]
            slice_cpu = Image.fromarray(slice_cpu)

            slice = trans(slice_cpu)
            slice = slice.unsqueeze(1)
            slice = slice.to(device)
            output = self.model(slice)

            output = torch.sigmoid(output).data.cpu().numpy()[0, :, :, :]
            output = output[0, :, :]
            output[output < 0.8] = 0
            output[output > 0] = 1

            output = ndimage.binary_fill_holes(output).astype(np.uint8)
            output = ndimage.binary_opening(output).astype(np.uint8)

            output = Image.fromarray(output)
            output = output.resize((predictions.shape[1], predictions.shape[2]), resample=Image.NEAREST)
            output = np.array(output)
            predictions[slice_nr, :, :] = output

            if self.show_plots:
                slice_cpu = slice_cpu.resize((predictions.shape[1], predictions.shape[2]), resample=Image.LINEAR)
                slice_cpu = np.array(slice_cpu)
                plt.clf()
                plt.figure(1)
                plt.imshow(slice_cpu, cmap='gray', interpolation=None)
                plt.imshow(output, cmap='jet', alpha=0.5, interpolation=None)
                plt.pause(0.0001)
            pbar.update(1)
        pbar.close()

        predictions = predictions.astype(np.uint8)
        predictions = np.transpose(predictions, (1, 2, 0))
        # for i in range(3):
        predictions = ndimage.binary_opening(predictions).astype(np.uint8)

        predictions = keep_largest(predictions)
        predictions = ndimage.binary_closing(predictions).astype(np.uint8)

        for i in range(5):
            ndimage.binary_fill_holes(predictions).astype(np.uint8) #, structure=np.ones((5,5))

        # predictions = ndimage.binary_dilation(predictions).astype(np.uint8)

        for i in range(3):
            predictions = np.rot90(predictions).copy()

        return predictions

def save(predictions, volume, case_id):
    # np.save(os.path.join('results', 'predictions.npy'), predictions)
    image_nii = nib.Nifti1Image(predictions, volume.affine)
    filename = 'predictions_{0}.nii'.format(case_id)
    # print(image_nii)
    nib.save(image_nii, os.path.join('results', filename))
    print('saved to ', filename)

def segment_case(case_loader, case_id):
    volume, segmentation = case_loader.load_case(case_id)
    segmentation = segmentation.get_fdata().astype(np.uint8)

    predictions = liver_segmenter.segment(volume)
    tk_dice, tu_dice = evaluate(predictions, segmentation)
    print(case_id, tk_dice, tu_dice)

    #predictions_tumor = tumor_segmenter.segment(volume, predictions)
    #predictions[predictions_tumor == 1] = 2

    tk_dice, tu_dice = evaluate(predictions, segmentation)
    print(case_id, tk_dice, tu_dice)
    predictions_nii = nib.Nifti1Image(predictions, volume.affine)

    return predictions_nii, tk_dice, tu_dice

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Segment image')
    parser.add_argument('--case-id', type=str, help='...')
    parser.add_argument('--show-plots', nargs='?', const=True, default=False, type=str2bool, help='...')
    parser.add_argument('--dataset-path', type=str, help='...')
    args = parser.parse_args()
    print(args)

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(device)

    liver_segmenter = LiverSegmenter(device, 'cas/planning/dl/weights/liver_weights.pth', args.show_plots)
    tumor_segmenter = TumorSegmenter(device, 'cas/planning/dl/weights/tumor_weights.pth', args.show_plots)

    case_loader = dataset.CaseLoader(args.dataset_path)
    predictions, tk_dice, tu_dice = segment_case(case_loader, args.case_id)
    nib.save(predictions, os.path.join(args.dataset_path, "case_{:05d}".format(int(args.case_id)), 'prediction.nii'))
