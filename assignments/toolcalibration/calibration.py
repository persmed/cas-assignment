import numpy as np


def pivot_calibration(transforms):
    """ Pivot calibration
    Keyword arguments:
    transforms -- A list with 4x4 transformation matrices,  (Fi)
    returns -- A vector p_t, which is the offset from any transform, Fi, to the pivot point
            -- The calibration matrix T (p_t in a 4X4 matrix form)  """

    ## TODO: Implement pivot calibration as discussed in the lecture
    p_t = np.zeros((3, 1))
    T = np.eye(4)

    return p_t, T

def calibration_device_calibration(camera_T_reference, camera_T_tracker, reference_P_pivot):
    """ Calibration device calibration
    Keyword arguments:
    camera_T_reference -- Transformation from the tool calibration device reference to the camera
    camera_T_tracker -- Transformation from the tool tracker to the camera
    reference_P_pivot -- A pivot on the calibration device reference (rigid body) where the tip of
                         the instrument is located for calibration
    returns -- The calibration matrix, tracker_T_pivot: i.e the tool tip location (reference_P_pivot) relative to the tracked tool (camera_T_tracker)
    """
    
    ## TODO: Implement a calibration method which uses a calibration device
    tracker_T_pivot = np.eye(4)
    
    return tracker_T_pivot
