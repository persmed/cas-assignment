Registration
============

Implement the paired points matching and iterative closest points (ICP) algorithms for patient to image
registration as discussed in lecture 6.

Theory
-------
.. image:: img/icp_animation.gif
   :scale: 50%
   :align: center

.. _Wikipedia: https://en.wikipedia.org/wiki/Iterative_closest_point

From Wikipedia_ the four steps in ICP are:

* For each point in the source point cloud, match the closest point in the reference point cloud (or a selected set).
* Estimate the combination of rotation and translation using a root mean square point to point distance metric minimization technique which will best align each source point to its match found in the previous step. This step may also involve weighting points and rejecting outliers prior to alignment.
* Transform the source points using the obtained transformation.
* Iterate (re-associate the points, and so on).

Paried points matching
-----------------------
As discussed in the lecture, ICP is basically an iteratively applied paired points matching algorithm. Therefore, you
will first implement the Paired points matching algorithm. The inputs are point clouds of corresponding points. You're
task is to calculate the transformation matrix that maps the source to the target point cloud.

.. code-block:: python
    :linenos:

    def paired_points_matching(source, target):
    """
    Calculates the transformation T that maps the source to the target
    :param source: A N x 3 matrix with N 3D points
    :param target: A N x 3 matrix with N 3D points
    :return:
        T: 4x4 transformation matrix mapping source onto target
        R: 3x3 rotation matrix part of T
        t: 1x3 translation vector part of T
    """

    T = np.eye(4)
    R = np.eye(3)
    t = np.zeros((1, 3))

    # Your code goes here

    return T, R, t


Iterative closest point
-----------------------
Now you have the basic building block of ICP so it's time to impalement the iteration part. Remember, that
initialization is crucial for ICP to work. You can either return a constant transformation for the initialization or
compute an initial transformation automatically. You also need to find the closest point to each source point

.. code-block:: python
    :linenos:

    def get_initial_pose(template_points, target_points):
        """
        Calculates an initial rough registration
        (Optionally you can also return a hand picked initial pose)
        :param source:
        :param target:
        :return: A transformation matrix
        """

    def find_nearest_neighbor(src, dst):

    def icp(source_points, target_points):
        """ Flood fill
        Keyword arguments:
        source_points --  ...
        target_points -- ...
        returns -- T...
        """
        # your code goes here


References
----------
* https://en.wikipedia.org/wiki/K-d_tree