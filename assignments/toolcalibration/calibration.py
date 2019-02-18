import numpy as np


def pivot_calibration(transforms):
    """ Pivot calibration
    Keyword arguments:
    transforms -- A list with 4x4 transformation matrices
    returns -- A vector p_t, which is the offset from any T to the pivot point
    """

    p_t = np.zeros((3, 1))
    T = np.eye(4)

    return p_t, T
