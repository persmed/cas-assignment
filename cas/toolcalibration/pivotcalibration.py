import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(sys.argv[0]), '../..'))

from assignments.toolcalibration import calibration


if __name__ == "__main__":
    import csv
    import numpy as np

    np.set_printoptions(suppress=True)

    transforms = list()

    with open('../../data/pivot_calibration/Tpointer2Cam.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            T = np.eye(4)
            data = np.loadtxt(row, delimiter=',')
            data = data.reshape((3, 4))
            T[:3, :4] = data
            transforms.append(T)

    p_t, T = calibration.pivot_calibration(transforms)

    print('Calibtration matrix T')
    print(T)
    print('Offset vector p_t: ')
    print(p_t)

    true_pt = np.asarray([[208.418, -0.643, -33.131]]).transpose()
    true_T = np.eye(4)
    true_T[:3, 3] = true_pt.T

    error = np.linalg.norm(T - true_T)
    print('Error of T')
    print(error)

    if error < 0.1:
        print("Successful")
    else:
        print("Check again")
