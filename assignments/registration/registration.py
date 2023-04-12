import numpy as np

def paired_point_matching(source, target):
    """
    Calculates the transformation T that maps the source to the target point clouds
    :param source: A N x 3 matrix with N 3D points
    :param target: A N x 3 matrix with N 3D points
    :return:
        T: 4x4 transformation matrix mapping source to target
        R: 3x3 rotation matrix part of T
        t: 1x3 translation vector part of T
    """
    assert source.shape == target.shape
    T = np.eye(4)
    R = np.eye(3)
    t = np.zeros((1, 3))

    ## TODO: your code goes here

    return T, R, t


def find_nearest_neighbor(src, dst):
    """
    Finds the nearest neighbor of every point in src in dst
    :param src: A N x 3 point cloud
    :param dst: A N x 3 point cloud
    :return: the index and distance of the closest point
    """

    ## TODO: replace this by your code
    pass


def icp(source, target, init_pose=None, max_iterations=10, tolerance=0.0001):
    """
    Iteratively finds the best transformation that mapps the source points onto the target
    :param source: A N x 3 point cloud
    :param target: A N x 3 point cloud
    :param init_pose: A 4 x 4 transformation matrix for the initial pose
    :param max_iterations: maximum number of iterations to perform, default is 10
    :param tolerance: maximum allowed error, default is 0.0001
    :return: A 4 x 4 rigid transformation matrix mapping source to target,
            the distances between each paired points, and the registration error
    """
    T = np.eye(4)
    distances = 0
    error = np.finfo(float).max

    ## TODO: Your code goes here

    return T, distances, error


def get_initial_pose(source, target):
    """
    Calculates an initial rough registration
    (Optionally you can also return a hand picked initial pose)
    :param source: A N x 3 point cloud
    :param target: A N x 3 point cloud
    :return: An initial 4 x 4 rigid transformation matrix mapping source to target
    """
    T = np.eye(4)

    ## TODO: Your code goes here

    return T

