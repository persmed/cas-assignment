import unittest
from cas.toolcalibration import pivotcalibration as calib

class TestStringMethods(unittest.TestCase):

    def test_split(self):
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

        p_t = calib.pivot_calibration(transforms)
        print(p_t)


if __name__ == '__main__':
    unittest.main()
