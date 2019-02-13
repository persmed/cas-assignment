import cas.registration.registration as registration
import numpy as np
import cas.registration.util as util


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
    # test_icp()
