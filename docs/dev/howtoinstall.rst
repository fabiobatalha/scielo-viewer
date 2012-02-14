=====================================
How to install a SciELO Viewer
=====================================

Install pre-requisites
----------------------

Before installing the SciELO Viewer application, install the software listed below.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Server software

 +-------------------------------------+-----------------------------------+-------------------------+--------------------------+
 |**software**                         |**product URL**                    |**installation method**  |**Ubuntu Package name**   |
 +=====================================+===================================+=========================+==========================+
 | Python 2.7                          | http://www.python.org/            | OS package manager      | python2.7                |
 +-------------------------------------+-----------------------------------+-------------------------+--------------------------+
 | python2.7                           | http://www.python.org/            | OS package manager      | python2.7-dev            |
 +-------------------------------------+-----------------------------------+-------------------------+--------------------------+
 | GNU compiler and tools              | http://www.python.org/            | OS package manager      | build-essential          |
 +-------------------------------------+-----------------------------------+-------------------------+--------------------------+
 | GIT                                 | http://git-scm.com/               | OS package manager      | git-core                 |
 +-------------------------------------+-----------------------------------+-------------------------+--------------------------+

 1. Install each package below using the recommended installation method above.

Note: Python comes pre-installed in most Linux distributions. If Python 2.5 or 2.6 is already installed, there is no need to install a newer version.

Note2: on Ubuntu 10.04 (Lucid) build-essential includes: dpkg-dev, g++, libc6-dev and make

System-wide Python libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 +-------------------+-------------------------------------------+------------------------------------------------------------------+
 |**software**       |**product URL**                            |**installation method**                                           |
 +===================+===========================================+==================================================================+
 | distribute 0.6.10 | http://pypi.python.org/pypi/distribute    | sudo python distribute_setup.py                                  |
 +-------------------+-------------------------------------------+------------------------------------------------------------------+
 | virtualenv        | http://pypi.python.org/pypi/virtualenv    | sudo easy_install virtualenv                                     |
 +-------------------+-------------------------------------------+------------------------------------------------------------------+
 | python gfx module | http://www.swftools.org/gfx_tutorial.html | installation instruction topic 1.1  Compiling gfx and installing |
 +-------------------+-------------------------------------------+------------------------------------------------------------------+

2. Download the distribute_setup.py script and use the installed Python interperter to run it as root (this provides the easy_install utility)::

    # wget http://python-distribute.org/distribute_setup.py
    # python distribute_setup.py


3. Use easy_install to download and install virtuaenv::

    # easy_install virtualenv