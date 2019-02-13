import csv
import numpy as np

import transformations


def read_data(filename):
    points = list()
    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            point = np.loadtxt(row, delimiter=',')
            points.append(point)

    return np.array(points)


def get_random_transformation_matrix():
    T = transformations.translation_matrix([5, 0, 10])
    R = transformations.rotation_matrix(0.123, [1, 0, 0])
    M = transformations.concatenate_matrices(T, R)
    return M


def get_random_point_clouds(N, T, dim=3, sigma=0.001):
    target = np.random.rand(N, dim)

    C = make_homogenous(target)

    source = np.dot(T, C.T).T
    source = source[:, :3]
    source += np.random.randn(N, dim) * sigma

    return target, source

def make_homogenous(M):
    N = M.shape[0]
    C = np.ones((N, 4))
    C[:, 0:3] = M
    return C