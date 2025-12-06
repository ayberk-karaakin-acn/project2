Installation
============

Requirements
------------

* Python 3.12 or higher
* Conda (recommended) or pip

Using Conda (Recommended)
--------------------------

1. Create the conda environment:

.. code-block:: bash

   conda env create -f environment.yml

2. Activate the environment:

.. code-block:: bash

   conda activate myapp

3. Install the package:

.. code-block:: bash

   pip install -e .

Using pip
---------

.. code-block:: bash

   pip install -e .

Development Installation
------------------------

To install with development dependencies:

.. code-block:: bash

   pip install -e ".[dev,test]"

Verifying Installation
----------------------

Verify the installation by running:

.. code-block:: bash

   myapp --version

You should see the version number displayed.

