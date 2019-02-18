import numpy as np
from scipy import ndimage

def region_grow(image, seed_point):
    """
    Performs a region growing on the image from seed_point
    :param image: An 3D grayscale input image
    :param seed_point: The seed point for the algorithm
    :return: A 3D binary segmentation mask with the same dimensions as image
    """
    segmentation_mask = np.zeros(image.shape, np.bool)
    z, y, x = seed_point
    threshold = image[z, y, x]
    print('data at ({0}, {1}, {2}) is {3}'.format(x, y, z, threshold))
    threshold_lower = threshold - 200
    threshold_upper = threshold + 200 
    segmentation_mask = (np.greater(image, threshold_lower)
                         & np.less(image, threshold_upper)).astype(np.bool)

    structure = np.ones((2, 2, 2))
    segmentation_mask= ndimage.binary_opening(segmentation_mask, structure=structure).astype(np.bool)
    # Your code goes here

    return segmentation_mask
