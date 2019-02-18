Python Installation
===================

.. role:: bash(code)
   :language: bash

The installation instructions here are based on those for MIA-Lab, so you can use it next semester as well.
https://mialab.readthedocs.io

To start with the installation, download the `Anaconda installer <https://www.anaconda.com/download/>`_ for your operating system and Python 3.7.

Windows
-------
The installation has been tested on Windows 10.

#. git installation

   - Download `git <https://git-scm.com/downloads>`_ and install

#. Clone CAS-Assignment repository

   - open "Git Bash"
   - :bash:`cd \path\to\where\you\want\the\code`
   - :bash:`git clone https://github.com/artorg-igt/cas-assignment.git`

#. Anaconda installation (`official website <https://docs.anaconda.com/anaconda/install/windows.html>`__)

   - Launch the installer
   - Select an install for "Just Me" unless you’re installing for all users (which requires Windows administrator privileges)
   - Choose whether to add Anaconda to your PATH environment variable. We recommend not adding Anaconda to the PATH environment variable, since this can interfere with other software.
   - Choose whether to register Anaconda as your default Python 3.6. Unless you plan on installing and running multiple versions of Anaconda, or multiple versions of Python, you should accept the default and leave this box checked.

#. Verify the installation

   - Open "Anaconda Prompt"
   - :bash:`conda list`, which should list all installed Anaconda packages

#. Create a new Python 3.7 environment with the name cas

   - :bash:`conda create -n cas python=3.7`

#. Activate the environment by

   - :bash:`activate cas`

#. Install some prerequisites first (apparently there are problems with numpy ans scipy on Windows)

   - Download the following packages from https://www.lfd.uci.edu/~gohlke/pythonlibs
      - numpy‑1.15.4+mkl‑cp37‑cp37m‑win_amd64.whl
      - scipy‑1.2.1‑cp37‑cp37m‑win_amd64.whl
   - :bash:`cd /path/to/cas-assignment/repository`
   - :bash:`pip install mkl`
   - :bash:`pip install /path/to/numpy‑1.15.4+mkl‑cp37‑cp37m‑win_amd64.whl`
   - :bash:`pip install /path/to/scipy‑1.2.1‑cp37‑cp37m‑win_amd64.whl`

#. Install all required packages for the CAS Assignments

   - :bash:`cd /path/to/cas-assignment/repository`
   - :bash:`pip install -r requirements.txt` will install all required packages.

#. Execute the installation test script to verify the installation

   - :bash:`python cas\test-installation.py`

Linux
------
Run the following commands in the terminal (tested on ubuntu 16.04 LTS).

#. git installation

   - :bash:`sudo apt-get install git`

#. Clone cas-assignment repository

   - :bash:`cd /path/to/where/you/want/the/code`
   - :bash:`git clone https://github.com/artorg-igt/cas-assignment.git`

#. Run Anaconda installation script (`official website <https://docs.anaconda.com/anaconda/install/linux>`__)

   - :bash:`bash <path_to_file>/Anaconda3-4.4.0-Linux-x86_64.sh` (run the installation script)

     - Scroll to the bottom of the license and enter :bash:`yes` to agree the license
     - Accept suggested installation path (or change it if you know what you do)
     - :bash:`yes` to add Anaconda to the PATH (and :bash:`no` to VisualCode installation)
     - Reopen the terminal

#. Verify the installation

   - :bash:`conda list`, which should list all installed Anaconda packages

#. Create a new Python 3.7 environment with the name cas (confirm with y when promted during creation)

   - :bash:`conda create -n cas python=3.7`

#. Activate the environment by

   - :bash:`source activate cas`

#. Install all required packages for the CAS assignments

   - :bash:`cd /path/to/cas-assignment/repository`
   - :bash:`pip install -r requirements.txt` will install all required packages (if the ``pydensecrf`` installation fails, install g++ by executing ``sudo apt-get install g++`` and ``sudo apt-get install python3.7-dev``)

#. Execute the hello world to verify the installation

   - :bash:`python cas/test_installation.py`


macOS
------
The installation has not been tested.

#. git installation

   - Download `git <https://git-scm.com/downloads>`_ and install

#. Clone cas-assignment repository

   - :bash:`cd /path/to/where/you/want/the/code`
   - :bash:`git clone https://github.com/artorg-igt/cas-assignment.git`

#. Anaconda installation (`official website <https://docs.anaconda.com/anaconda/install/mac-os>`__)

   - Launch the installer
   - On the Destination Select screen, select "Install for me only"
   - (Don't install VisualStudio Code)
   - etc.

#. Verify the installation

   - :bash:`conda list`, which should list all installed Anaconda packages

#. Create a new Python 3.7 environment with the name cas

   - :bash:`conda create -n cas python=3.7`

#. Activate the environment by

   - :bash:`source activate cas`

#. Install all required packages for the CAS Assignments

   - :bash:`cd /path/to/cas-assignment/repository`
   - :bash:`pip install -r requirements.txt` will install all required packages

#. Execute the hello world to verify the installation

   - :bash:`python cas/test_installation.py`
