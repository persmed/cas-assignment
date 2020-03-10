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

    camera_T_tracker = transformations.concatenate_matrices(
        transformations.translation_matrix([20, 100, 0]),
        transformations.rotation_matrix(np.pi/4, [0, 0, -1]))
    print('camera_T_tracker\r\n', camera_T_tracker)

    reference_P_pivot = transformations.concatenate_matrices(
        transformations.translation_matrix([5, 5, 0]),
        transformations.rotation_matrix(np.pi, [0, 0, 1]))
    print('reference_P_pivot\r\n', reference_P_pivot)

    tracker_T_pivot = calibration.calibration_device_calibration(
        camera_T_reference, camera_T_tracker, reference_P_pivot)
    print('tracker_T_pivot\r\n', tracker_T_pivot)

    # sanity check
    T_check = camera_T_reference @ reference_P_pivot @ np.linalg.inv(tracker_T_pivot) @ np.linalg.inv(camera_T_tracker)
    print('Check (should be identity\r\n', T_check)
    check = (T_check.shape[0] == T_check.shape[1]) and np.allclose(T_check, np.eye(T_check.shape[0]))
    print('Sanity check passed: ', check)
