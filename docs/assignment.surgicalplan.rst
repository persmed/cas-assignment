Surgical Planning
=================

In this assignment, you are tasked with developing a segmentation algorithm. Your goal is to segment the pelvis, lumbar vertebrae, intervertebral discs, and the spinal cord within a CT dataset.

**Objective:** Implement a region growing algorithm to perform the segmentation, following the guidelines provided in lectures.

.. image:: img/result-assignment1.png
   :scale: 50%
   :align: center


Setup
-----

- **Data Preparation:** Transfer the ``pelvis_ct.nii.gz`` file from ILIAS to ``data/planning/pelvis_ct.nii.gz``.
- **Update Repository:** Update your repository by running ``git pull --autostash``.
- **Implementation File:** The ``segmentation.py`` file within ``assignments/planning/`` directory contains a rough implementation. Complete the sections marked with ``## TODO:``.

  .. include:: ../assignments/planning/segmentation.py
     :start-line: 5
     :literal:
     :code: python

- **Execution:** Run your segmentation script via ``python cas/planning/planning.py`` to segment the specified structures. The segmentation does not need to be perfect, but the structures should be separated (see the 3D view above).


Testing your algorithm
----------------------

Execute the ``planning.py`` script to test your algorithm. Use keyboard shortcuts to interact with the application, perform segmentation by clicking (several times), and save your work.

The script opens a window with a CT scan of a pelvis and spine model. The following keyboard shortcuts are available:

- ``1-4`` select active label. The segmented region (output of your algorithm) will then be labelled with the active label:

   0. None (default)
   1. Spinal cord
   2. Vertebrae
   3. Pelvis
   4. Discs

- ``click`` to start the region growing segmentation at the cursor position (seed point)
- ``space`` toggle segmentation mask overlay
- ``up`` or ``scroll`` move slice up
- ``down`` or ``scroll`` move slice down
- ``v`` visualise the resulting 3D surface models for the current segmentation mask
- ``r`` reset segmentation mask to zero
- ``s`` save segmentation mask to disk
- ``q`` quit (without saving)


Saving the output
-----------------

- Save the completed segmentation to disk using the ``s`` key.
- Verify the saved segmentation mask by running the script ``show3d.py`` for a 3D visualisation: ``python cas/planning/show3d.py``. The script will load and display the segmentation saved to disk.
- Create and save a screenshot of the 3D segmented models.


Code Submission
---------------

Submit a ZIP file named ``lastname_firstname_assignment1.zip`` on ILIAS containing:

#. The modified ``segmentation.py`` as ``lastname_firstname_assignment1_code.py``.
#. Console output in a text file named ``lastname_firstname_assignment1_output.txt``.
#. A screenshot of the 3D segmented model as ``lastname_firstname_assignment1_screenshot.png``.


Online Questions
----------------

Complete the "Assignment 1 - Questions" on ILIAS:

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


Resources
---------

- `SciPy multidimensional image processing documentation <https://docs.scipy.org/doc/scipy/reference/ndimage.html>`_
