Assignment Environment Setup
============================

Follow the setup instructions and install the environment
(see :doc:`installation.python` and :doc:`installation.ide`).

Download the file ``pelvis_ct.nii.gz`` from the Assignment 0 page on ILIAS and
copy it to:

``data/planning/pelvis_ct.nii.gz``

Run the installation test
-------------------------

Choose one of the following options.

Option A: Run from the command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   :linenos:

   python cas/test_installation.py

Option B: Run from PyCharm
~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Open ``cas/test_installation.py`` in PyCharm.
#. Select the ``cas`` run configuration (created in :doc:`installation.ide`).
#. Click the green *Run* button.

If everything is set up correctly, the script prints version information and
finishes with:

``Your environment is ready.``

Submission
----------

Upload a text file with the output from the previous command onto ILIAS.

Name the file as ``firstname_lastname_assignment0.txt``.

Grading
-------

This setup activity is not graded. It is required to ensure that your
environment is ready for Assignment 1.