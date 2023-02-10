======
Purify
======
.. image:: https://img.shields.io/badge/python-3.10-blue
    :target: https://www.python.org/
    :alt: Recommended Python version
.. image:: https://img.shields.io/badge/flask-2.2.2-green
    :target: https://flask.palletsprojects.com/
    :alt: Flask version: 2.2.2
.. image:: https://img.shields.io/badge/app-purify-brightgreen
    :target: https://github.com/Andrej2003/purify
    :alt: App Purify
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
directory using sqlite3. It reads all the data then returns it
and its' column names on the ``/api`` or ``/api/companies-data``
endpoint. It also has an ``/api/companies-data/purify`` endpoint
which writes the new cleaned data in a MongoDB database.
The calls_api.py makes request calls to the API endpoints.




Technologies
------------
**Python 3.10 (recommended)**

The project is created with:

Backend:

* Flask version: 2.2.2
* requests version: 2.28.1
* pymongo version: 4.3.3

Frontend:

* Jinja2 version: 3.1.2
* Bootstrap version: 5.3.0
* DataTables version: 1.13.1


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
