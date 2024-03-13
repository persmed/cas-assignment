import numpy as np


def pivot_calibration(transforms):
    """
    Pivot calibration

    Keyword arguments:
    transforms -- A list of 4x4 transformation matrices from the tracking system (Fi)
                  representing the tracked tool's position and orientation at
                  different instances.

    Returns:
    T          -- The calibration matrix T (in homogeneous coordinates) that defines
                  the offset (p_t) from the tracked part to the pivot point (tool tip).
    """

    ## TODO: Implement pivot calibration as discussed in the lecture

    T = np.eye(4)

    return T


def calibration_device_calibration(camera_T_reference, camera_T_tool, reference_T_tip):
    """
    Tool calibration using calibration device

    Keyword arguments:
    camera_T_reference -- Transformation matrix from reference (calibration device) to camera.
    camera_T_tool      -- Transformation matrix from tool to camera.
    reference_T_tip    -- Transformation matrix from tip to reference (calibration device).

    Returns:
    T                  -- Calibration matrix from tool to tip.
    """

    ## TODO: Implement a calibration method which uses a calibration device

    T = np.eye(4)
    
    return T
