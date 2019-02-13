Registration
============

.. image:: img/icp_animation.gif

Implement the iterative closest points (ICP) algorithm for patient to image
registration

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
Now you have the building blocks of ICP so it's time to impelemt the iteration part. Remember, that initialization is
crucial for ICP to work. You can either return a constant transformation for the initalization or compute an initial
transformation automatically. You also need to find the closest point to each source point

.. code-block:: python
    :linenos:

    def get_initial_pose(template_points, target_points):
        """

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