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
            # print(T)
            transforms.append(T)

    p_t, T = pivot_calibration(transforms)
    # p_t = np.round(p_t, decimals=3)
    # T = np.round(T, de)
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
