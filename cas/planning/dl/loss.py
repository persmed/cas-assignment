import torch
import torch.nn as nn


def dice_loss(pred, target, smooth=1.):
    pred = pred.contiguous()
    target = target.contiguous()

    intersection = (pred * target).sum(dim=2).sum(dim=2)

    loss = (1 - ((2. * intersection + smooth) / (pred.sum(dim=2).sum(dim=2) + target.sum(dim=2).sum(dim=2) + smooth)))
    # print(loss.shape)
    return loss.mean()

def weighted_dice_coef(pred, target, weights):
    pred = pred.clone()#.contiguous()
    target = target.clone()#.contiguous()

    w_0 = weights[0]
    w_1 = weights[1]

    pred_0 = (1 - pred)
    target_0 = (1 - target)

    intersection_0 = torch.sum(pred_0 * target_0)
    intersection_1 = torch.sum(pred * target)

    return 2 * (w_0 * intersection_0 + w_1 * intersection_1) \
        / ((w_0 * (torch.sum(target_0) + torch.sum(pred_0))) +
         (w_1 * (torch.sum(target) + torch.sum(pred))))

if __name__ == "__main__":
    input = torch.zeros(5, 5)
    input[:, 0] = 1
    input[:, 1] = 0

    target = input.clone()

    dice_coeff = weighted_dice_coef(input, target, (0.5, 0.5))
    print(dice_coeff)

    input[:, 3] = 1
    print(input, '\n', target)
    dice_coeff = weighted_dice_coef(input, target, (1, 1))
    print(dice_coeff)

    dice_coeff = weighted_dice_coef(input, target, (10, 1))
    print(dice_coeff)

    dice_coeff = weighted_dice_coef(input, target, (1, 5))
    print(dice_coeff)
