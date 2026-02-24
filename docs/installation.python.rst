Python Installation
===================

.. role:: bash(code)
   :language: bash

The installation instructions here are based on the MIALab setup, so you can
reuse a similar workflow next semester as well:
`MIALab documentation <https://mialab.readthedocs.io/>`_

To start with the installation, download and install
`Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_
for your operating system.

.. note::

   If you already have Miniconda or Anaconda installed, you can skip the Miniconda
   installation step. The course commands stay the same.

:ref:`Windows <install-windows>` | :ref:`Linux <install-linux>` | :ref:`macOS <install-macos>`

.. _install-windows:

Windows
-------
The installation has been tested on Windows 10 and 11.

#. Install git

   - Download `git <https://git-scm.com/downloads>`_ and install

#. Clone CAS-Assignment repository

   - Open "Git Bash"
   - :bash:`cd /path/to/where/you/want/the/code`
   - :bash:`git clone https://github.com/persmed/cas-assignment.git`
   - :bash:`cd cas-assignment`

#. Miniconda installation (`official website <https://docs.conda.io/en/latest/miniconda.html>`__)

   - Launch the Miniconda installer
   - Select an install for "Just Me" unless you’re installing for all users
     (which requires Windows administrator privileges)
   - Choose whether to add Miniconda to your PATH environment variable. We
     recommend not adding it to PATH, since this can interfere with other
     software.
   - Choose whether to register Miniconda as your default Python. Unless you
     plan on installing and running multiple Python distributions, you should
     accept the default and leave this box checked.

#. Verify the installation

   - Open "Miniconda Prompt"
   - :bash:`conda list`, which should list installed conda packages

#. Create a new Python environment with all dependencies

   - :bash:`conda env create --file environment.yml`

#. (Optional) If you are using PowerShell instead of the command prompt run

   - :bash:`conda init powershell`

#. Activate the environment by

   - :bash:`conda activate cas`

   .. note::

      If ``conda activate`` does not work, run :bash:`conda init` once, then close
      and reopen the terminal.

#. Execute the installation test script to verify the installation

   - :bash:`python cas/test_installation.py`

   .. note::

      The installation test requires the file ``data/planning/pelvis_ct.nii.gz``.
      If it is missing, ``cas/test_installation.py`` will stop and print
      instructions on where to place the file.

      Download and copy the file by following :doc:`assignment.setup`.

.. _install-linux:

Linux
------
The installation has been tested on Ubuntu 16.04 LTS (should also work on newer Ubuntu versions).

#. git installation

   - :bash:`sudo apt-get install git`

#. Clone cas-assignment repository

   - :bash:`cd /path/to/where/you/want/the/code`
   - :bash:`git clone https://github.com/persmed/cas-assignment.git`
   - :bash:`cd cas-assignment`

#. Run Miniconda installation script (`official website <https://docs.conda.io/en/latest/miniconda.html>`__)

   - Download the Miniconda installer for your architecture, then run for example:
     :bash:`bash <path_to_file>/Miniconda3-latest-Linux-x86_64.sh`

     - Scroll to the bottom of the license and enter :bash:`yes` to agree the license
     - Accept suggested installation path (or change it if you know what you do)
     - :bash:`yes` to initialize Miniconda (adds conda to your shell)
     - Reopen the terminal

#. Verify the installation

   - :bash:`conda list`, which should list installed conda packages

#. Create a new Python environment with all dependencies

   - :bash:`conda env create --file environment.yml`

#. Activate the environment

   - :bash:`conda activate cas`

   .. note::

      If ``conda activate`` does not work, run :bash:`conda init` once, then close
      and reopen the terminal.

#. Execute the installation test script to verify the installation

   - :bash:`python cas/test_installation.py`

   .. note::

      The installation test requires the file ``data/planning/pelvis_ct.nii.gz``.
      If it is missing, ``cas/test_installation.py`` will stop and print
      instructions on where to place the file.

      Download and copy the file by following :doc:`assignment.setup`.

.. _install-macos:

macOS
------
The installation has been tested on macOS 10.13.6 (should also work on newer macOS versions).

#. git installation

   - Download `git <https://git-scm.com/downloads>`_ and install

#. Clone cas-assignment repository

   - :bash:`cd /path/to/where/you/want/the/code`
   - :bash:`git clone https://github.com/persmed/cas-assignment.git`
   - :bash:`cd cas-assignment`

#. Miniconda installation (`official website <https://docs.conda.io/en/latest/miniconda.html>`__)

   - Download and run the Miniconda installer for macOS (Intel or Apple Silicon,
     depending on your machine)
   - Follow the installer steps
   - Reopen the terminal

#. Verify the installation

   - :bash:`conda list`, which should list installed conda packages

#. Create a new Python environment with all dependencies

   - :bash:`conda env create --file environment.yml`

#. Activate the environment

   - :bash:`conda activate cas`

   .. note::

      If ``conda activate`` does not work, run :bash:`conda init` once, then close
      and reopen the terminal.

#. Execute the installation test script to verify the installation

   - :bash:`python cas/test_installation.py`

   .. note::

      The installation test requires the file ``data/planning/pelvis_ct.nii.gz``.
      If it is missing, ``cas/test_installation.py`` will stop and print
      instructions on where to place the file.

      Download and copy the file by following :doc:`assignment.setup`.