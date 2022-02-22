import numpy as np


def pivot_calibration(transforms):
    """ Pivot calibration
    Keyword arguments:
    transforms -- A list with 4x4 transformation matrices,  (Fi)
    returns -- The calibration matrix T (p_t in homogeneous cordinate form) where the vector p_t, is the offset from any transform, Fi, to the pivot point """
      
    ## TODO: Implement pivot calibration as discussed in the lecture

    T = np.eye(4)

    return T

def calibration_device_calibration(F, camera_T_tracker, reference_P_pivot):
    """ Calibration device calibration
    Keyword arguments:
    F -- Transformation from the tool calibration device reference to the camera, camera_T_reference
    camera_T_tracker -- Transformation from the tool tracker to the camera
    reference_P_pivot -- A pivot on the calibration device reference (rigid body) where the tip of
                         the instrument is located for calibration
    returns -- The calibration matrix, T: i.e the tool tip location (reference_P_pivot) relative to the tracked tool (camera_T_tracker)
    """
    
    ## TODO: Implement a calibration method which uses a calibration device
    
    T = np.eye(4)
    
    return T
