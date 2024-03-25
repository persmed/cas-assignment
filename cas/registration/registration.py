import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(sys.argv[0]), '../..'))

import numpy as np
np.set_printoptions(suppress=True, threshold=10)

import matplotlib
matplotlib.use("TkAgg")
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import cas.registration.util as util
from assignments.registration import registration


def on_pick(event):
    ind = event.ind[0]
    x_picked, y_picked, z_picked = event.artist._offsets3d
    x_center, y_center, z_center = x_picked[ind], y_picked[ind], z_picked[ind]
    picked_point = (x_center, y_center, z_center)

    ax = plt.gca()
    ax.set_title(f"Picked point coordinates: {picked_point}")

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    zlim = ax.get_zlim()

    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]
    z_range = zlim[1] - zlim[0]

    ax.set_xlim(x_center - x_range / 2, x_center + x_range / 2)
    ax.set_ylim(y_center - y_range / 2, y_center + y_range / 2)
    ax.set_zlim(z_center - z_range / 2, z_center + z_range / 2)

    plt.draw()


def on_key(event):
    if event.key == 'q':
        return

    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    zlim = ax.get_zlim()

    zoom_in_factor = 0.9
    zoom_out_factor = 1.1

    # Determine zoom direction: 'in' with the up arrow, 'out' with the down arrow
    if event.key == 'up':
        ax.set_xlim([xlim[0]*zoom_in_factor, xlim[1]*zoom_in_factor])
        ax.set_ylim([ylim[0]*zoom_in_factor, ylim[1]*zoom_in_factor])
        ax.set_zlim([zlim[0]*zoom_in_factor, zlim[1]*zoom_in_factor])
    elif event.key == 'down':
        ax.set_xlim([xlim[0]*zoom_out_factor, xlim[1]*zoom_out_factor])
        ax.set_ylim([ylim[0]*zoom_out_factor, ylim[1]*zoom_out_factor])
        ax.set_zlim([zlim[0]*zoom_out_factor, zlim[1]*zoom_out_factor])

    plt.draw()


def test_paired_point_matching():
    print('\n---------------------')
    print('PAIRED POINT MATCHING')
    print('---------------------\n')

    N = 5
    T_random = util.get_random_transformation_matrix()
    target, source = util.get_random_point_clouds(N, T_random)

    print(f'Target point cloud\n{target}\n')
    print(f'Source point cloud\n{source}\n')

    T, R, t = registration.paired_point_matching(source, target)

    source_H = util.make_homogenous(source)
    source_T = np.dot(T, source_H.T).T[:, :3]
    error = np.linalg.norm(source_T - target)

    print(f'Transformed source point cloud\n{source_T}\n')
    print(f'Transformation\n{T}\n')
    print(f'Error\n{error}\n')

    if error < 0.1:
        print("Success: error < 0.1")
    else:
        print("Failure: error >= 0.1. Please review your code.")


def test_icp():
    print('\n-----------------------')
    print('ITERATIVE CLOSEST POINT')
    print('-----------------------\n')

    target_points = util.read_data('data/registration/TargetPoints.csv')
    print(f'Target point cloud\n{target_points}\n')

    template_points = util.read_data('data/registration/TemplatePoints.csv')
    print(f'Source point cloud\n{template_points}\n')

    T_rot_x = registration.get_initial_pose(template_points, target_points)
    T, d, error = registration.icp(template_points, target_points, init_pose=T_rot_x)

    template_points_T = util.make_homogenous(template_points)
    template_points_T = np.dot(T, template_points_T.T).T[:, :3]

    print(f'Transformed source point cloud\n{template_points_T}\n')
    print(f'Transformation\n{T}\n')
    print(f'Error\n{error}\n')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    sample_choice = np.random.choice(target_points.shape[0], 1000)
    samples = target_points[sample_choice, :]

    ax.scatter(samples[:, 0], samples[:, 1], samples[:, 2], c='b', marker='.', picker=5)
    ax.scatter(template_points_T[:, 0], template_points_T[:, 1], template_points_T[:, 2], c='r', marker='x', picker=5)

    fig.canvas.mpl_connect('pick_event', on_pick)
    fig.canvas.mpl_connect('key_press_event', on_key)

    ax.set_title(f"Click on a point to display its coordinates!")
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    # plt.axis([-3, 3, -3, 3])
    plt.axis('equal')
    plt.show()


if __name__ == "__main__":
    test_paired_point_matching()
    test_icp()
