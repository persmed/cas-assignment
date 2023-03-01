Python Installation
===================

.. role:: bash(code)
   :language: bash

The installation instructions here are based on those for MIALab, so you can use it next semester as well.
https://mialab.readthedocs.io

To start with the installation, download the `Anaconda installer <https://www.anaconda.com/download/>`_ for your operating system.

Windows
-------
The installation has been tested on Windows 10 and 11.

#. Install git

   - Download `git <https://git-scm.com/downloads>`_ and install

#. Clone CAS-Assignment repository

   - open "Git Bash"
   - :bash:`cd \path\to\where\you\want\the\code`
   - :bash:`git clone https://github.com/persmed/cas-assignment.git`
   - :bash:`cd cas-assignment`

#. Anaconda installation (`official website <https://docs.anaconda.com/anaconda/install/windows.html>`__)

   - Launch the installer
   - Select an install for "Just Me" unless you’re installing for all users (which requires Windows administrator privileges)
   - Choose whether to add Anaconda to your PATH environment variable. We recommend not adding Anaconda to the PATH environment variable, since this can interfere with other software.
   - Choose whether to register Anaconda as your default Python. Unless you plan on installing and running multiple versions of Anaconda, or multiple versions of Python, you should accept the default and leave this box checked.

#. Verify the installation

   - Open "Anaconda Prompt"
   - :bash:`conda list`, which should list all installed Anaconda packages

#. Create a new Python environment with all dependencies

   - :bash:`conda env create --file environment.yml`

#. (Optional) If you are using PowerShell instead of the command prompt run

   - :bash:`conda init powershell`

#. Activate the environment by

   - :bash:`conda activate cas`

#. Execute the installation test script to verify the installation

   - :bash:`python cas/test_installation.py`

Linux
------
Run the following commands in the terminal (tested on ubuntu 16.04 LTS).

#. git installation

   - :bash:`sudo apt-get install git`

#. Clone cas-assignment repository

   - :bash:`cd /path/to/where/you/want/the/code`
   - :bash:`git clone https://github.com/persmed/cas-assignment.git`
   - :bash:`cd cas-assignment`

#. Run Anaconda installation script (`official website <https://docs.anaconda.com/anaconda/install/linux>`__)

   - :bash:`bash <path_to_file>/Anaconda3-4.4.0-Linux-x86_64.sh` (run the installation script)

     - Scroll to the bottom of the license and enter :bash:`yes` to agree the license
     - Accept suggested installation path (or change it if you know what you do)
     - :bash:`yes` to add Anaconda to the PATH (and :bash:`no` to VisualCode installation)
     - Reopen the terminal

#. Verify the installation

   - :bash:`conda list`, which should list all installed Anaconda packages

#. Create a new Python environment all dependencies

   - :bash:`conda env create --file environment.yml`

#. Activate the environment by

   - :bash:`source activate cas`

#. Execute the hello world to verify the installation

   - :bash:`python cas/test_installation.py`


macOS
------
The installation has been tested on macOS High Sierra (10.13.6).

#. git installation

   - Download `git <https://git-scm.com/downloads>`_ and install

#. Clone cas-assignment repository

   - :bash:`cd /path/to/where/you/want/the/code`
   - :bash:`git clone https://github.com/persmed/cas-assignment.git`
   - :bash:`cd cas-assignment`

#. Anaconda installation (`official website <https://docs.anaconda.com/anaconda/install/mac-os>`__)

   - Launch the installer
   - On the Destination Select screen, select "Install for me only"
   - (Don't install VisualStudio Code)
   - etc.

#. Verify the installation

   - :bash:`conda list`, which should list all installed Anaconda packages

#. Create a new Python environment with all dependencies

   - :bash:`conda env create --file environment.yml`

#. Activate the environment by

   - :bash:`source activate cas`

#. Execute the hello world to verify the installation

   - :bash:`python cas/test_installation.py`
