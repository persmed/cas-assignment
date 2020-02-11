import argparse
import numpy as np
import nibabel as nib
import numpy as np

LABELS = {
    "Liver": 1,
    "Tumor": 2
}

def calc_volume(image, label, spacing):
    """
    Calculates the volume of an object with the label
    :param image: A 3D segmented volume
    :param label: The label for which the volume shall be computed
    :param spacing: The voxel spacing of the image
    :return: The volume of the object
    """
    volume = 0

    #TODO: implement code to calculate the volume in mL

    return volume

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate volume')
    parser.add_argument('--case-id', type=str, help='...')
    parser.add_argument('--dataset-path', type=str, help='...')
    args = parser.parse_args()
    print(args)

    filename = 'predictions_{0}.nii'.format(case_id)
    input_image = os.path.join(agrs.dataset_path, filename)

    input_image = nib.load(input_image)
    input_image = input_image.get_fdata().astype(np.float32)

    spacing = [volume.affine[0][0], volume.affine[1][1], volume.affine[2][2]]
    volume_liver = calc_volume(input_image, LABELS["Liver"], spacing)
    volume_tumors = calc_volume(input_image, LABELS["Tumor"], spacing)

    print("Liver volume: {0}".format(volume_liver))
    print("Tumor volume: {0}".format(volume_tumors))
