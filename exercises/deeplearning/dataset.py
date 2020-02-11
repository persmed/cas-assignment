import sys
import os
import json
from os.path import dirname
from pathlib import Path
import nibabel as nib
from nibabel.processing import resample_to_output
import numpy as np
import torch
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image
np.set_printoptions(precision = 3, suppress = True)
import scipy.ndimage as ndimage


class CaseLoader:
    def __init__(self, case_folder, imaging_file = 'imaging.nii', segmentation_file = 'segmentation.nii'):
        self.case_folder = case_folder
        self.imaging_file = imaging_file
        self.segmentation_file = segmentation_file
        pass

    def __str__(self):
        return 'case_folder: {0}'.format(self.case_folder)

    def get_full_case_id(self, cid):
        try:
            cid = int(cid)
            case_id = "case_{:05d}".format(cid)
        except ValueError:
            case_id = cid

        return case_id

    def get_all_cases(self):
        cases = []
        dataset_file = os.path.join(self.case_folder, 'lits.json')
        with open(dataset_file) as json_file:
            data_file = json.load(json_file)
            for dat in data_file:
                case_id = dat['case_id']
                cases.append(case_id)
        return cases

    def get_case_path(self, cid):
        # Resolve location where data should be living
        if not os.path.isdir(self.case_folder):
            raise IOError(
                "Data path, {}, could not be resolved".format(str(data_path))
            )

        # Get case_id from provided cid
        case_id = self.get_full_case_id(cid)

        # Make sure that case_id exists under the data_path
        case_path = os.path.join(self.case_folder, case_id)
        if not os.path.isdir(case_path):
            raise ValueError(
                "Case could not be found \"{}\"".format(case_path)
            )

        return case_path


    def load_volume(self, cid):
        case_path = self.get_case_path(cid)
        vol = nib.load(os.path.join(case_path, self.imaging_file))
        return vol


    def load_segmentation(self, cid):
        case_path = self.get_case_path(cid)
        seg = nib.load(os.path.join(case_path, self.segmentation_file))
        return seg


    def load_case(self, cid):
        vol = self.load_volume(cid)
        seg = self.load_segmentation(cid)
        return vol, seg


class LiTSDataSet(Dataset):
    def __init__(self, dataset_path, dataset_file, cases=None, transforms=None, zoom=1, dilation=False):
        self.case_loader = CaseLoader(dataset_path)
        self.cases = []
        if cases is not None:
            self.cases = cases
        else:
            with open(dataset_file) as json_file:
                data_file = json.load(json_file)
                for dat in data_file:
                    case_id = dat['case_id']
                    self.cases.append(case_id)

        self.transforms = transforms
        self.zoom = zoom
        self.dilation = dilation

    def __len__(self):
        return len(self.cases)

    def __getitem__(self, idx):
        case_id = self.cases[idx]
        vol, seg = self.case_loader.load_case(case_id)

        volume = vol.get_fdata().astype(np.float32)
        segmentation = seg.get_fdata().astype(np.float32)

        volume = ndimage.zoom(volume, zoom=[self.zoom, self.zoom, 1], order=0)
        segmentation = ndimage.zoom(segmentation, zoom=[self.zoom, self.zoom, 1], order=0)

        if self.dilation:
            segmentation2 = ndimage.binary_dilation(segmentation).astype(np.uint8)
            for i in range(5):
                segmentation2 = ndimage.binary_dilation(segmentation2).astype(np.uint8)
            segmentation2[segmentation == 2.0] = 2
            segmentation = segmentation2.astype(np.float32)

        volume = np.rot90(volume).copy()
        segmentation = np.rot90(segmentation).copy()

        if self.transforms is not None:
            volume = self.transforms(volume)
            segmentation = self.transforms(segmentation)

        # volume = volume.type(torch.FloatTensor)
        # segmentation = segmentation.type(torch.ByteTensor)

        return volume, segmentation

def get_lits_data_loaders(dataset_path, dataset_file, transforms, split_ratio, batch_size, zoom, dilation):
    train_cases = np.loadtxt('train_cases.txt', delimiter=",", dtype=np.str)
    test_cases = np.loadtxt('test_cases.txt', delimiter=",", dtype=np.str)

    train_dataset = LiTSDataSet(dataset_path, dataset_file, train_cases,
                              transforms=transforms, zoom=zoom, dilation=dilation)

    test_dataset = LiTSDataSet(dataset_path, dataset_file, test_cases,
                            transforms=transforms, zoom=zoom, dilation=dilation)

    # train_size = int(split_ratio * len(dataset))
    # test_size = len(dataset) - train_size
    # train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_size, test_size])

    dataloaders = {
        'train': DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=1),
        'val': DataLoader(test_dataset, batch_size=batch_size, shuffle=True, num_workers=1),
        'n_train': len(train_dataset),
        'n_val': len(test_dataset)
    }
    return dataloaders

if __name__ == "__main__":
    dataset_path = '/home/ubelix/artorg/paolucci/datasets/lits/cases'
    case_loader = CaseLoader(dataset_path)
    print(case_loader)

    vol, seg = case_loader.load_case('case_00003')
    # print(vol)
    print(seg.shape)

    # vol_resampled = resample_to_output(vol, [1, 1, 1], order=0)
    # print(vol_resampled.shape)

    dataset_file = os.path.join(dataset_path, 'lits.json')
    data_set = LiTSDataSet(dataset_path, dataset_file,
                            transforms=transforms.Compose([transforms.ToTensor()]))
    print(data_set)

    vol, seg = data_set[2]
    print(vol.shape, vol.dtype)
    print(seg.shape, seg.dtype)

    print(vol.min(), vol.max())
    print(seg.min(), seg.max())
