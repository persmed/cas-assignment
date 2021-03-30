Tool Calibration
################

This assignment is based on the lecture "Postional Tracking", where you will implement two different ways to calibrate a tool.

Pivot calibration
*****************

Implement the pivot calibration algorithm as discussed in the "Positional Tracking" lecture.

Theory
======

.. image:: img/pivot_calibration.png

* :math:`p_t` is constant if looking from tool local COS
* Pivot point (tool tip) :math:`p_p` is constant if looking from the tracking COS
* At any moment, :math:`F_i(R_i, p_i)` can be retrieved from the tracker API
* :math:`F_i(R_i, p_i)` takes :math:`p_t` to :math:`p_p`
* :math:`R_i \cdot p_t + p_i = p_p`
* Unknowns: :math:`p_t` and :math:`p_p`

Programming assignment
======================

Implement the pivot calibration algorithm in the file ``assignments/toolcalibration/calibration.py``. You can test your implementation by running
the file directly in PyCharm or from the console using ```python cas/toolcalibration/pivotcalibration.py``.

.. code-block:: python
    :linenos:

    def pivot_calibration(transforms):
        """ Pivot calibration
        Keyword arguments:
        transforms -- A list with 4x4 transformation matrices
        returns -- A vector p_t, which is the offset from any T to the pivot point
        """

        ## TODO: Implement pivot calibration as discussed in the lecture
        p_t = np.zeros((3, 1))
        T = np.eye(4)

        return p_t, T

Calibration device
******************

Implement the code to calibrate an instrument using a calibration device.

Theory
======

.. image:: img/calibdevice.png

The following transformations are given:

* :math:`^{Camera}T_{Tracker}` : transformation from the tracker to the camera (given by the tracking system)
* :math:`^{Camera}T_{Reference}` : transformation from the reference to the camera (given by the tracking system)
* :math:`^{Reference}T_{Pivot}` : transformation from the pivot hole to the reference (given by the CAD model)

The following transformation is missing:

* :math:`^{Tracker}T_{Pivot}` : calibration transformation from the tool tip to the tracker

To implement these calculations you can use the following definition:

.. math::

    I = ^{Camera}T_{Tracker} \cdot ^{Tracker}T_{Pivot} \cdot ^{Pivot}T_{Reference} \cdot ^{Reference}T_{Camera}

Thus, if you multiply all transformations in the same direction you get an identity.

Note: If you use the * operator Python will perform a element-wise matrix multiplication!

Programming assignment
======================
You have to implement this algorithm in the file ``assignments/toolcalibration/calibration.py``. You can test your implementation by running
the file directly in PyCharm or from the console using ```python cas\toolcalibration\calibrationdevice.py``.

.. code-block:: python
    :linenos:

    def calibration_device_calibration(camera_T_reference, camera_T_tracker, reference_P_pivot):
        """ Calibratio device calibration
        Keyword arguments:
        camera_T_reference -- Transformation from the reference to the camera
        camera_T_tracker -- Transformation from the tracker to the camera
        reference_P_pivot -- A pivot on the reference (rigid body) where the tip of
                             the instrument is located for calibration
        """
        
        ## TODO: Implement a calibration method which uses a calibration device
        tracker_T_pivot = np.eye(4)
        
        return tracker_T_pivot

Questions
*********

Write a short document (max 1 page) where you address the following questions:

#. In which coordinate system is the vector :math:`p_t`
#. Write down the formula to get the tip of the pointer in the camera coordinate system
#. Where does the error in your result come from (what you get is not the exact solution which is provided)?
#. How many degrees of freedeom can you calibrate with pivoting? Which ones are missing?
#. If your instrument is non-rigid (e.g. a needle) your :math:`p_t` is off if your instrument is bent. How can you overcome this issue?

Submission
**********
Send a ZIP file with the follwing files:

#. Your document as PDF with filename ``lastname_firstname_assignment3_report.pdf``
#. Your code with filename ``lastname_firstname_assignment3_code.py``
#. A text file with the console output when you ran the code with filename ``lastname_firstname_assignment3_output.txt``

Name your ZIP file as ``lastname_firstname_assignment3.zip``

Grading
*******

The assignment accounts for 25% of the grade for the assignments.

You can get 10 Points in this assignment:


- Working code and a correct result gives you 5 pts

  * Important: We don't grade the code quality, but it would be nice if we don't have to spend hours to understand it
- If the code does not work, but you gave it at least a decent try you get 2.5 pts
- For each correctly answered question you get 1 pt


Materials
*********

- https://docs.scipy.org/doc/numpy/reference/routines.linalg.html#solving-equations-and-inverting-matrices
- https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-465
- https://docs.scipy.org/doc/numpy/reference/generated/numpy.matmul.html
