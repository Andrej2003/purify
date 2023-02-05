======
Purify
======
.. image:: https://img.shields.io/badge/python-3.10-blue
   :alt: Recommended Python version
Big Data Purification (Company Names) with Flask Application

Table of Contents
-----------------
* `Overview`_
* `Technologies`_
* `Setup`_
* `Key Features`_

Overview
--------
The Flask application connects to a database in the relative
directory using sqlite3 and reads all the data then returns
a list of it and its' column names on the ``/api`` or
``/api/companies-data`` endpoint.

Technologies
------------
**Python 3.10 (recommended)**

The project is created with:

* Flask version: 2.2.2
* Jinja2 version: 3.1.2
* requests version: 2.28.1
* pymongo version: 4.3.3


Setup
-----
To set up the app run the following command:

.. code-block::

    pip install -r requirements.txt

Key Features
------------
* removes legal entity suffix
* removes parentheses and text in them
* capitalizes the company/business name
