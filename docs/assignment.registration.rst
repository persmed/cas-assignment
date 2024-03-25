Registration
============
In this assignment, you will implement the paired point matching (PPM) and iterative closest point (ICP) algorithms for patient-to-image
registration as discussed in the "Registration" lecture.

Theory
-------
.. image:: img/icp_animation.gif
   :scale: 50%
   :align: center

From `Wikipedia <https://en.wikipedia.org/wiki/Iterative_closest_point>`_, the four steps in ICP are:

#. For each point in the source point cloud, match the closest point in the reference point cloud (or a selected set).
#. Estimate the combination of rotation and translation using a root mean square point to point distance metric minimization technique which will best align each source point to its match found in the previous step. This step may also involve weighting points and rejecting outliers prior to alignment.
#. Transform the source points using the obtained transformation.
#. Iterate (re-associate the points, and so on).

Paired Point Matching
---------------------
As discussed in the lecture, ICP is essentially an iterative application of the paired point matching algorithm. Your first task is to implement this algorithm in the file ``assignments/registration/registration.py``. You are given point clouds of corresponding points and must calculate the transformation matrix that maps the source to the target point clouds.

.. code-block:: python
    :linenos:

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

Test your implementation by running the script in PyCharm or from the console using ``python cas/registration/registration.py``.

Iterative Closest Point
-----------------------

With the basic building block of ICP in place, implement the iterative part of the algorithm in the same Python file. This script will open a Matplotlib figure to help visualise the results. You can interactively navigate the plot using the `commands provided by Matplotlib <https://matplotlib.org/stable/users/explain/figure/interactive.html#interactive-navigation>`_.

Initial pose
____________


Provide an initial pose by estimating it from the data or selecting it manually.

.. code-block:: python
    :linenos:

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

Find the Closest Point
______________________

Implement a function to find the closest point in the target data for each point in the source data. It is recommended to use a KD-tree for efficiency (see `Resources`_).

Your function should return a tuple of two arrays: the first containing the distances to the nearest neighbor in the target for each point in the source, and the second containing the indices of these nearest neighbors in the target.

.. code-block:: python
    :linenos:

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

Iterative Matching
__________________

Implement the iterative matching process that applies the paired point matching until your error function converges.

.. code-block:: python
    :linenos:

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


Code Submission
---------------

Submit a ZIP file named ``lastname_firstname_assignment3.zip`` on ILIAS containing:

#. The modified ``registration.py`` as ``lastname_firstname_assignment3_code.py``.
#. Console output in a text file named ``lastname_firstname_assignment3_output.txt``.
#. A screenshot of the plots as ``lastname_firstname_assignment3_screenshot.png``.

Online Questions
----------------

Complete the "Assignment 3 - Questions" on ILIAS:

- Answer all questions.
- Each question has only one correct answer.
- All questions are equally weighted. Incorrect answers will not result in point deductions.
- You are allowed only one attempt to complete the test.

Assignment Evaluation
---------------------

This assignment constitutes 25% of your total assignment grade, split equally between:

- **Code Evaluation (50%)**: points are awarded as follows:

   - **4 points** for a working solution.
   - **3 points** for only small errors.
   - **2 points** for a substantial effort.
   - **1 point** for substantial errors or minimal effort.
   - **0 points** for no attempt or plagiarism.

- **Online questions (50%)**

.. _resources:

Resources
---------

KD-Trees
________

You don't neccessarily need to use them, but it will make the search for the closest point faster.

* https://en.wikipedia.org/wiki/K-d_tree
* https://scikit-learn.org/stable/modules/neighbors.html
* https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.query.html

Solving systems of equations
____________________________

* https://docs.scipy.org/doc/numpy/reference/routines.linalg.html#solving-equations-and-inverting-matrices
* https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.svd.html#numpy.linalg.svd
