Registration
============
In this assignment, you will implement the paired point matching (PPM) and iterative closest point (ICP) algorithms for patient to image
registration as discussed in lecture "registration".

Theory
-------
.. image:: img/icp_animation.gif
   :scale: 50%
   :align: center

.. _Wikipedia: https://en.wikipedia.org/wiki/Iterative_closest_point

From Wikipedia_ the four steps in ICP are:

#. For each point in the source point cloud, match the closest point in the reference point cloud (or a selected set).
#. Estimate the combination of rotation and translation using a root mean square point to point distance metric minimization technique which will best align each source point to its match found in the previous step. This step may also involve weighting points and rejecting outliers prior to alignment.
#. Transform the source points using the obtained transformation.
#. Iterate (re-associate the points, and so on).

Paired point matching
---------------------
As discussed in the lecture, ICP is basically an iteratively applied paired point matching algorithm in the file ``assignments/registration/registration.py``. Therefore, you
will first implement the paired point matching algorithm. The inputs are point clouds of corresponding points. Your
task is to calculate the transformation matrix that maps the source to the target point clouds.

.. code-block:: python
    :linenos:

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

        return T, R, t

You can test your implementation by running the file directly in PyCharm or from the console using ``python cas/registration/registration.py``.

Iterative closest point
-----------------------

You now have the basic building block of ICP, so it is time to implement the iteration part in the file ``assignments/registration/registration.py``. 
Remember that initialisation is crucial for ICP to work. You can test your implementation by running the file directly in PyCharm or from the console using ``python cas/registration/registration.py``.

Initial pose
____________

First, you have to give an initial pose. For that it is easiest to just look at the data and give a rough estimate.


.. code-block:: python
    :linenos:

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

Find the closest point
______________________

Second, you need to fine the closest point of each point in the source data to the target data. It is recommended to
use a KD-tree for that, as it is easier to implement (you can use a library, see links below) and faster.

.. code-block:: python
    :linenos:

    def find_nearest_neighbor(src, dst):
        """
        Finds the nearest neighbor of every point in src in dst
        :param src: A N x 3 point cloud
        :param dst: A N x 3 point cloud
        :return: the
        """

        ## TODO: replace this by your code
        pass

Iterative matching
__________________

Lastly, you actually have to implement the iteration itself. Do the last two steps and apply paired point matching
until your error function converges.

.. code-block:: python
    :linenos:

    def icp(source, target, init_pose=None, max_iterations=10, tolerance=0.0001):
        """
        Iteratively finds the best transformation that mapps the source points onto the target
        :param source: A N x 3 point cloud
        :param target: A N x 3 point cloud
        :param init_pose: A 4 x 4 transformation matrix for the initial pose
        :param max_iterations: maximum number of iterations to perform, default is 10
        :param tolerance: maximum allowed error, default is 0.0001
        :return: A 4 x 4 rigid transformation matrix mapping source to target,
                the distances between each paired point, and the registration error
        """
        T = np.eye(4)
        distances = 0
        error = 0

        ## TODO: Your code goes here

        return T, distances, error

Questions
---------

Write a short document (max 1 page) where you address the following questions:

#. What happens if you use an identity as initial pose?
#. Name two methods you could use to initialise ICP?
#. Describe two methods allowing you to acquire the target point cloud (on the therapeutic object) in the OR.
#. What is the minimum number of points you need for paired point matching?
#. If the patient moves, the calculated transformation is not accurate anymore. How can you prevent this from happenning?

Submission
----------
Send a ZIP file with the follwing files:

#. Your report as PDF with filename ``lastname_firstname_assignment3_report.pdf``
#. Your code with filename ``lastname_firstname_assignment3_code.py``
#. A textfile with the console output when you ran the code with filename ``lastname_firstname_assignment3_output.txt``
#. A screenshot of the plots ``lastname_firstname_assignment3_screenshot.png``

Name your ZIP file as ``lastname_firstname_assignment4.zip`` and upload it to ILIAS.

Grading
-------

The assignment accounts for 25% of the grade for the assignments.

You can get 10 Points in this assignment:

* Working code and a correct result gives you 5 pts
   * Important: We don't grade the code quality, but it would be nice if we don't have to spend hours to understand it
* If the code does not work, but you gave it at least a decent try you get 2.5 pts
* For each correctly answered question you get 1 pt

Materials
----------

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
