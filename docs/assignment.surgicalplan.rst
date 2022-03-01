Surgical Planning
=================

In this assignment you will implement a segmentation algorithm to segment the pelvis, lumbar vertebrae, intervertebral discs and the spinal cord from a CT dataset.

.. image:: img/result-assignment1.png
   :scale: 50%
   :align: center


Region Growing
--------------

In this assignment you have to implement a region growing algorithm, as discussed in the lecture, in the file ``assignments/planning/segmentation.py``.
Before you implement the code, copy the ``pelvis_ct.nii.gz`` data into ``data/planning/pelvis_ct.nii.gz``. In ``segmentation.py``, you are already provided with a rough implementation of the algorithm. You mainly have to complete code in lines with a ``## TODO:`` tag.

.. include:: ../assignments/planning/segmentation.py
   :start-line: 5
   :code: python

To do the segmentation you can run ``python cas/planning/planning.py``, see details below. For this assignment you are required to segment the Bone structures (pelvis, vertebraes), the intervertebral discs and the spinal cord. This will lead to a 3D view like the one above. Also, the segmentation doesn't need to be perfect, but the structures should be well separated.


Testing your algorithm
----------------------

To test your algorithm, you can run the file ``cas/planning/planning.py`` in the IDE or you run it on the console with ``python cas/planning/planning.py``.

The scripts opens a window with a CT scan of a pelvis and spine model. The following keyboard shortcuts are available:

- ``0-4`` select active label. The segmented region (output of your algorithm) will then be labelled with the active label.
   0. none (default)
   1. spinal cord
   2. vertebraes
   3. pelvis
   4. discs
- ``click`` start region growing segmentation at cursor position (seed point)
- ``space`` toggle segmentation mask overlay
- ``up`` move slice up
- ``down`` move slice down
- ``s`` save segmentation mask and screenshot
- ``r`` reset segmentation mask to zero
- ``q`` quit (without saving)

Once you have your segmentation, save it using the ``s`` key. Then use the script ``show3d.py`` to visualize your segmentation in a 3D viewer: ``python cas/planning/show3d.py``.


Report
------
Write a short report (max 1 page) where you address the following questions:

#. On your segmentation mask, two vertebraes are connected by 1 voxel. Which morphological operator could you use to separate these two regions?
#. Your CT image has salt & pepper noise. How would you preprocess the image to improve your segmentation?
#. You want to plan a trajectory for a pedicle screw placement on your 3D model. What information do you need to define this trajectory?
#. Which algorithm can you use to get a surface model from your segmentation?


Submission
----------
Upload a ZIP file containing the following files to ILIAS:

#. Your report as PDF with filename ``lastname_firstname_assignment1_report.pdf``
#. Your code with filename ``lastname_firstname_assignment1_code.py``
#. A textfile with the console output when you ran the code with filename ``lastname_firstname_assignment1_output.txt``
#. A file with a screenshot of the 3D rendering of your segmentation with filename ``lastname_firstname_assignment1_screenshot.png``

Name your ZIP file as ``lastname_firstname_assignment1.zip``


Grading
-------

The assignment accounts for 25% of the grade for the assignments.

You can get 10 points in this assignment:

* Working code and a correct result gives you 5 pts
   * Important: We don't grade the code quality, but it would be nice if we don't have to spend hours to understand it
* If the code does not work, but you gave it at least a decent try you get 2.5 pts
* For each correctly answered question you get 1.25 pt


Materials
---------
* https://docs.scipy.org/doc/scipy/reference/ndimage.html
