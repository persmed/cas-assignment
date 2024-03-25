import numpy as np

def paired_point_matching(source, target):
    """
    Calculates the transformation T that maps the source to the target point clouds.
    :param source: A N x 3 matrix with N 3D points.
    :param target: A N x 3 matrix with N 3D points.
    :return:
        T: 4x4 transformation matrix mapping source to target.
        R: 3x3 rotation matrix part of T.
        t: 1x3 translation vector part of T.
    """
    assert source.shape == target.shape
    T = np.eye(4)
    R = np.eye(3)
    t = np.zeros((1, 3))

    ## TODO: your code goes here

    return T, R, t


def get_initial_pose(source, target):
    """
    Calculates an initial rough registration or optionally returns a hand-picked initial pose.
    :param source: A N x 3 point cloud.
    :param target: A N x 3 point cloud.
    :return: An initial 4 x 4 rigid transformation matrix.
    """
    T = np.eye(4)

    ## TODO: Your code goes here

    return T


def find_nearest_neighbor(source, target):
    """
    Finds the nearest neighbor in 'target' for every point in 'source'.
    :param source: A N x 3 point cloud.
    :param target: A N x 3 point cloud.
    :return: A tuple containing two arrays: the first array contains the
             distances to the nearest neighbor in 'target' for each point
             in 'source', and the second array contains the indices of
             these nearest neighbors in 'target'.
    """

    ## TODO: replace this by your code
    pass


def icp(source, target, init_pose=None, max_iterations=10, tolerance=0.0001):
    """
    Iteratively finds the best transformation mapping the source points onto the target.
    :param source: A N x 3 point cloud.
    :param target: A N x 3 point cloud.
    :param init_pose: Initial pose as a 4 x 4 transformation matrix.
    :param max_iterations: Maximum iterations.
    :param tolerance: Error tolerance.
    :return: The optimal 4 x 4 rigid transformation matrix, distances, and registration error.
    """

    # Initialisation
    T = np.eye(4)
    distances = 0
    error = np.finfo(float).max

    ## TODO: Your code goes here

    return T, distances, error
