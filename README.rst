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
The Flask application connects to a database in the relative directory using sqlite3. 
It reads all the data then returns it and its' column names on the ``/api`` or ``/api/companies-data`` endpoint. 
It also has an ``/api/companies-data/purify`` endpoint which writes the new cleaned data in a MongoDB database.
The calls_api.py makes request calls to the API endpoints.

In calls_api there are two functions:

1. clean_names - takes a list of the company names then cleans them from legal entity suffixes (such as “limited”, “ltd”, “ltd.”, “c.i.c”, “llc”), then removes parentheses, text in them and capitalizes the name
2. write_data - this function takes the clean data as an argument then makes a POST request to write the data in the database with the clean company name as the key and a dictionary of the company attributes (“id”, “country_iso”, “city”, “nace” and “website”) as the value

The project has a front-end which is available at the following routes:

* ``/``  
* ``/companies-data``
* ``/companies-data/purify``

There are two buttons that show the original and purified data in a table which has searching, number of entries per page and pagination.



Key Features
------------
* Removes legal entity suffix
* Deletes parentheses and text in them
* Capitalizes the company name

Technologies
------------
**Python 3.10 (recommended)**

The project is created with:

**Backend:**

* Flask version: 2.2.2
* requests version: 2.28.1
* pymongo version: 4.3.3

**Frontend:**

* Jinja2 version: 3.1.2
* Bootstrap version: 5.3.0
* DataTables version: 1.13.1


Setup
-----
To set up and run the app use the following commands:

.. code-block::

    pip install -r requirements.txt

* To run ``app.py`` use the command:

.. code-block::

    python3 app.py

* To run ``calls_api.py`` use the command:

.. code-block::

    python3 calls_api.py

Before using the commands above install  `MongoDB
<https://www.mongodb.com/try/download/community>`_
