import os
import sys
import transformations
import numpy as np
np.set_printoptions(suppress=True)

sys.path.insert(0, os.path.join(os.path.dirname(sys.argv[0]), '../..'))

from assignments.toolcalibration import calibration


if __name__ == "__main__":
    camera_T_reference = transformations.concatenate_matrices(
        transformations.translation_matrix([50, 20, 0]),
        transformations.rotation_matrix(np.pi/2, [0, 0, 1]))
    print('camera_T_reference\r\n', camera_T_reference)

    camera_T_tool = transformations.concatenate_matrices(
        transformations.translation_matrix([20, 100, 0]),
        transformations.rotation_matrix(np.pi/4, [0, 0, -1]))
    print('camera_T_tool\r\n', camera_T_tool)

    reference_T_tip = transformations.concatenate_matrices(
        transformations.translation_matrix([5, 5, 0]),
        transformations.rotation_matrix(np.pi, [0, 0, 1]))
    print('reference_T_tip\r\n', reference_T_tip)

    tool_T_tip = calibration.calibration_device_calibration(
        camera_T_reference, camera_T_tool, reference_T_tip)
    print('tool_T_tip\r\n', tool_T_tip)

    # sanity check
    T_check = camera_T_reference @ reference_T_tip @ np.linalg.inv(tool_T_tip) @ np.linalg.inv(camera_T_tool)
    print('Check (should be identity)\r\n', T_check)
    check = (T_check.shape[0] == T_check.shape[1]) and np.allclose(T_check, np.eye(T_check.shape[0]))
    print('Sanity check passed: ', check)
