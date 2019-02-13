Python Installation
===================

.. role:: bash(code)
   :language: bash

To start with the installation, download the `Anaconda installer <https://www.anaconda.com/download/>`_ for your operating system and Python 3.6.


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

#. Install all required packages for the CAS Assignments

   - :bash:`cd /d /path/to/cas-assignment/repository`
   - :bash:`pip install .` will install all required packages.

#. Execute the installation test script to verify the installation

   - :bash:`python .\bin\test-install.py`

#. (Optional) Run Sphinx to create the documentation

   - :bash:`sphinx-build -b html .\docs .\docs\_build`
   - The documentation is now available under ``.\docs\_build\index.html``
