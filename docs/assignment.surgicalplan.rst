Surgical Planning
=================

Implement a segmentation algorithm to segment the pelvis, lumbar vertebrae and intervertebral discs.

Theory
-------


Programming assignment
----------------------

In this assignment you have to implement a region growing algorithms in the file ``cas/planning/segmentation.py``.


.. code-block:: python
    :linenos:


    def region_grow(image, seed_point):
        """
        Performs a region growing on the image from seed_point
        :param image: An 3D grayscale input image
        :param seed_point: The seed point for the algorithm
        :return: A 3D binary segmentation mask with the same dimensions as image
        """
        segmentation_mask = np.zeros(image.shape, np.bool)

        # Your code goes here

        return segmentation_mask

Testing your algorithm
______________________

To test your algorithm, you can run the file ``cas/planning/planning.py`` in the IDE or you run it on the console with
``python cas/planning/planning.py``.

The scripts opens a window with a CT scan of a pelvis and spine model. You can use 'Space' to toggle the segmentation
overlay. Using the keys 0 - 4, you can change the active label:

0. None
1. Sacrum
2. Pelvis
3. L4
4. L5

By clicking on the image, you start the segmentation with the location as the seed point. The segmented region (output
of your algorithm) will then be labelled with the active label.

Report
------
Write a short report (max 1 page) where you address the following questions:

#.
#.
#.
#.

Submission
----------
Send a ZIP file with the follwing files:

#. Your report as PDF with filename [firstname lastname]_assignment1_report.pdf
#. Your code with filename [firstname lastname]_assignment1_code.py
#. A textfile with the console output when you ran the code with filename [firstname lastname]_assignment1_output.txt
#. A file with a screenshot of the 3D rendering of your segmentation with filename [firstname lastname]_assignment1_screenshot.png

Name your ZIP file as ``firstname_lastname_assignment1.zip``

References
----------
