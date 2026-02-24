Integrated Development Environment (PyCharm)
============================================

`JetBrains PyCharm <https://www.jetbrains.com/pycharm/>`_ is a suitable IDE for the Python assignments.
The **Community Edition** is free and sufficient for this course.

Install PyCharm by following the official guide:
`PyCharm Installation Instructions <https://www.jetbrains.com/help/pycharm/requirements-installation-and-launching.html>`_

.. note::

   The screenshots below are from Windows. On macOS the menu path is typically
   *PyCharm > Settings* instead of *File > Settings*.

Prerequisites
-------------

Before you start in PyCharm, make sure you have:

- downloaded or cloned the repository ``cas-assignment``
- created the conda environment called ``cas`` (as described in :doc:`installation.python`)

Open the assignment as a PyCharm project
----------------------------------------

#. Start PyCharm.
#. Click *Open* (or *File > Open*).
#. Select the folder ``cas-assignment`` (the repository root), then confirm.

   .. image:: img/pycharm_setup_1.png
      :width: 690px
      :align: center

Configure the Python interpreter (conda environment ``cas``)
------------------------------------------------------------

PyCharm must use the conda environment ``cas`` to find the required libraries.

#. Open the settings:

   - Windows/Linux: *File > Settings...*
   - macOS: *PyCharm > Settings...*

   .. image:: img/pycharm_setup_2.png
      :width: 690px
      :align: center

#. In the left sidebar, go to *Python > Interpreter*.

   .. image:: img/pycharm_setup_3.png
      :width: 690px
      :align: center

#. If ``cas`` is already available in the interpreter dropdown, select it.
   Otherwise add it:

   - click *Add Interpreter*
   - choose *Add Local Interpreter...*

   .. image:: img/pycharm_setup_3.png
      :width: 690px
      :align: center

#. In *Add Python Interpreter*:

   - select *Select existing*
   - set *Type* to *Conda*
   - set *Environment* to your ``cas`` environment folder, for example:

     - Windows: ``C:\Users\<username>\miniconda3\envs\cas``
     - Linux/macOS: ``/home/<username>/miniconda3/envs/cas``

   - click *OK*

   .. image:: img/pycharm_setup_4.png
      :width: 690px
      :align: center

#. Back in *Python > Interpreter*, confirm that:

   - the selected interpreter points to ``.../envs/cas/...``
   - you see many installed packages in the list

   Then click *OK* to close the settings.

   .. image:: img/pycharm_setup_5.png
      :width: 690px
      :align: center

Create a run configuration (recommended)
----------------------------------------

Create one run configuration that always uses the ``cas`` interpreter and runs
the currently opened file. This avoids accidentally running code with the wrong
Python environment.

#. Open ``cas/test_installation.py`` (Project view on the left).
#. Open the run configuration dialog:

   - In the top bar, open the configuration dropdown (often shows *Current File*)
   - Click *Edit Configurations...*

   .. image:: img/pycharm_setup_6.png
      :width: 690px
      :align: center

#. Create a new configuration:

   - Click *Add new run configuration...*
   - Select *Python*

   .. image:: img/pycharm_setup_7.png
      :width: 690px
      :align: center

#. Define the configuration:

   - **Name**: ``cas``
   - **Interpreter**: select your conda environment ``cas``
   - **script**: ``$FilePathRelativeToProjectRoot$`` (this runs whichever file is currently open)
   - **Working directory**: ``</path/to/cas-assignment>``

   Click *OK*.

   .. image:: img/pycharm_setup_8.png
      :width: 690px
      :align: center

Verify your setup in PyCharm
----------------------------

#. Make sure the run configuration ``cas`` is selected in the top bar.
#. With ``cas/test_installation.py`` open, click the green *Run* button.

   .. image:: img/pycharm_setup_9.png
      :width: 690px
      :align: center

.. note::

   The installation test requires the file ``data/planning/pelvis_ct.nii.gz``.
   If it is missing, ``cas/test_installation.py`` will stop and print
   instructions on where to place the file.

   Download and copy the file by following :doc:`assignment.setup`.

Important
---------

Before running any assignment code, make sure the ``cas`` run configuration
is selected. Otherwise PyCharm may run using a different interpreter.

Troubleshooting (most common issues)
------------------------------------

- **ImportError / ModuleNotFoundError**
  Verify that *Python > Interpreter* points to ``envs/cas`` and that the run
  configuration uses the same interpreter.

- **File not found (relative paths to data)**
  Verify that the run configuration *Working directory* is set to the repository
  root ``cas-assignment``.