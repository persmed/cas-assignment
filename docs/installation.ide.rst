Integrated Development Environment (IDE)
========================================

We recommend to use `JetBrains PyCharm <https://www.jetbrains.com/pycharm/>`_ as IDE to program in Python.
The community edition is open-source and sufficient for our purposes.
Follow the `instructions <https://www.jetbrains.com/help/pycharm/requirements-installation-and-launching.html>`_ to install PyCharm.

To open the CAS Assignment as a project and to configure the Python interpreter do the following:

#. Launch PyCharm
#. Click Open (or File > Open)

    #. In the dialog navigate to ``</path/to/where/you/have/the/code>/cas-assignment``
    #. Click OK
    #. CAS Assignment is now open as PyCharm project (PyCharm created the ``.idea`` directory)

#. Click File > Settings... to open the settings dialog

    #. Navigate to Project: CAS Assignment > Project Interpreter
    #. Select the Python interpreter ``</path/to/your/anaconda/installation>/envs/cas/bin/python`` (on Linux and macOS) or ``<\path\to\your\anaconda\installation>\envs\mialab\python.exe`` (on Windows)

        - If the interpreter is not available in the combo box, click the gear icon and choose Add Local and navigate the the files above

    #. Confirm by clicking OK

#. Open the ``test_installation.py`` (``cas`` directory) in the navigator

    #. Right click in the editor > Run 'test_installation'
    #. Runs the test_installation and adds a configuration (see top right corner) to the project
    #. You can add configurations manually under Run > Edit Configurations...

#. For each assignment, make sure your working directory is set to ``</path/to/where/you/have/the/code>/cas-assignment``

You can watch the `getting started <https://www.jetbrains.com/pycharm/documentation/>`_ videos to get accustomed with the interface.
