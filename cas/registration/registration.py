import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(sys.argv[0]), '../..'))

import numpy as np
np.set_printoptions(suppress=True)

import matplotlib
matplotlib.use("TkAgg")
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



import cas.registration.util as util
from assignments.registration import registration


def test_icp():
    target_points = util.read_data('data/registration/TargetPoints.csv')
    print(target_points)

    template_points = util.read_data('data/registration/TemplatePoints.csv')
    print(template_points)

    T_rot_x = registration.get_initial_pose(template_points, target_points)
    T, d, error = registration.icp(template_points, target_points, init_pose=T_rot_x)

    template_points_T = util.make_homogenous(template_points)
    template_points_T = np.dot(T, template_points_T.T).T[:, :3]

    print(template_points_T)

    print(T)

    print(error)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    sample_choice = np.random.choice(target_points.shape[0], 1000)
    # print(sample_choice)
    samples = target_points[sample_choice, :]
    ax.scatter(samples[:, 0], samples[:, 1], samples[:, 2], c='b', marker='.')
    # ax.scatter(template_points[:, 0], template_points[:, 1], template_points[:, 2], c='g', marker='x')
    ax.scatter(template_points_T[:, 0], template_points_T[:, 1], template_points_T[:, 2], c='r', marker='x')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    # plt.axis([-3, 3, -3, 3])
    plt.axis('equal')
    plt.show()


def test_paired_points_matching():
    N = 5
    T_random = util.get_random_transformation_matrix()
    target, source = util.get_random_point_clouds(N, T_random)

    print('Target point cloud\n', target, '\n')

    T, R, t = registration.paired_points_matching(source, target)

    source_H = util.make_homogenous(source)
    source_T = np.dot(T, source_H.T).T[:, :3]
    print('Source point cloud\n', source_T, '\n')
    error = np.linalg.norm(source_T - target)

    print('Transformation\n', T, '\n')

    print('Error\n', error, '\n')

    if error < 0.1:
        print("Successful")
    else:
        print("Check again")

    return


if __name__ == "__main__":
    test_paired_points_matching()
    test_icp()
