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
----------------------
As discussed in the lecture, ICP is basically an iteratively applied paired points matching algorithm. Therefore, you
will first implement the Paired points matching algorithm.

.. code-block:: python
    :linenos:

    def paired_points_matching(source, target):
    """

    :param source:
    :param target:
    :return:
        T: 4x4 transformation matrix mapping source onto target
        R: 3x3 rotation matrix part of T
        t: 1x3 translation vector part of T
    """

Iterative closest point
-----------------------
Now you have the basic building block of ICP so it's time to implement the iteration part. Remember, that
initialization is crucial for ICP to work.

Initial pose
____________
First, you have to give an initial pose. For that it's easiest to just look at the data and give a rough estimate.
You can also calculate one based from the data automatically, but this is optional.

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

Find the closest point
______________________
Second, you need to fine the closest point of each point in the source data to the target data. It is recommendet to
use a KD-tree for that, as it is easier to implement (you can use a library) and faster.

.. code-block:: python
    :linenos:

    def find_nearest_neighbor(src, dst):
        """
        Finds the nearest neighbor of every point in src in dst
        :param src: A N x 3 point cloud
        :param dst: A N x 3 point cloud
        :return: the
        """

Iterative matching
__________________

Lastly, you actually have to implement the iteration itself. Do the last two steps and apply paired points matching
your errorfunction converges.

.. code-block:: python
    :linenos:

    def icp(source_points, target_points):
        """
        Iteratively finds the best transformation that mapps the source points onto the target
        :param source: A N x 3 point cloud
        :param target: A N x 3 point cloud
        :param init_pose: A 4 x 4 transformation matrix for the initial pose
        :param max_iterations: default 10
        :param tolerance: maximum allowed error
        :return: A 4 x 4 rigid transformation matrix mapping source to target
                the distances and the error
        """
        # your code goes here

Report
------

Write a short report (max 1 page) where you address the following questions:

#. What happens if you use an identity as initial pose?
#. Describe two methods, how you can acquire the target data in the OR.
#. What is the minimum number of points you need for paired points matching?
#. If the patient moves, your calculated transformation is not accurate anymore. How can you prevent this?
#. We are in ENT surgery now. Which anatomical landmarks do you take for paired points matching and which surface for ICP. Explain why?

Submission
----------
Send a ZIP file with the follwing files:

#. Your report as PDF with filename [firstname lastname]_assignment3_report.pdf
#. Your code with filename [firstname lastname]_assignment3_code.py
#. A textfile with the console output when you ran the code with filename [firstname lastname]_assignment3_output.txt

Name your ZIP file as ``firstname_lastname_assignment3.zip`` and upload it to ILIAS before the deadline.


Materials
----------
* https://en.wikipedia.org/wiki/K-d_tree