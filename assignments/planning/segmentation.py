import numpy as np
from scipy import ndimage
import queue


def region_grow(image, seed_point):
    """
    Performs a region growing on the image from seed_point
    :param image: An 3D grayscale input image
    :param seed_point: The seed point for the algorithm
    :return: A 3D binary segmentation mask with the same dimensions as image
    """
    segmentation_mask = np.zeros(image.shape, np.bool)

    return segmentation_mask
