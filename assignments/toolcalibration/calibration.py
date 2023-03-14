import numpy as np


def pivot_calibration(transforms):
    """ Pivot calibration
    Keyword arguments:
    transforms -- A list of 4x4 transformation matrices from the tracking system (Fi)
    returns    -- The calibration matrix T (p_t in homogeneous coordinate form),
                  where the vector p_t, is the offset from any transform, Fi, to the pivot point
    """

    ## TODO: Implement pivot calibration as discussed in the lecture

    T = np.eye(4)

    return T


def calibration_device_calibration(camera_T_reference, camera_T_tool, reference_P_pivot):
    """ Tool calibration using calibration device
    Keyword arguments:
    camera_T_reference -- Transformation from the reference (calibration device) to the camera
    camera_T_tool      -- Transformation from the tool to the camera
    reference_P_pivot  -- A pivot point on the calibration device reference (rigid body),
                          where the tip of the instrument is located for calibration
    returns            -- The tool tip location (p_t or reference_P_pivot) and the
                          calibration matrix (T), i.e. the tool tip location
                          (reference_P_pivot) relative to the tracked tool (camera_T_tool)
    """
    
    ## TODO: Implement a calibration method which uses a calibration device
    
    T = np.eye(4)
    
    return T
