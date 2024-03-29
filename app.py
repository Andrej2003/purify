import sqlite3
import pymongo
import json
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path="/static")


@app.route('/')
@app.route('/companies-data', methods=["GET"])
def read_data_template():
    """
    Renders a template (or view) for the companies-data endpoint.

    :return: str
    """

    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM companies")
    data = cursor.fetchall()
    column_names = [name[0] for name in cursor.description]
    return render_template("index.html", data=data, columns=column_names)


@app.route('/api')
@app.route('/api/companies-data', methods=["GET"])
def read_data():
    """
    GET method

    Returns a list containing the data and column names on the api/companies-data endpoint.

    :return:  list
    """

    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM companies")
    data = cursor.fetchall()
    column_names = [name[0] for name in cursor.description]
    return [data, column_names]


@app.route('/companies-data/purify', methods=["GET"])
def write_data_view():
    """
    Renders a template (or view) for the companies-data/purify endpoint.

    :return: str
    """

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['purified_data']['companies']
    data = [x for x in db.find({}, {"_id": 0})]
    columns = ["name", "id", "country_iso", "city", "nace", "website"]
    return render_template("purified.html", data=data, columns=columns)


@app.route('/api/companies-data/purify', methods=["POST"])
def write_data():
    """
    POST method

    Writes the purified data in the MongoDB database.

    :return: str
    """

    clean_data = json.loads(request.json)

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['purified_data']
    companies = db["companies"]
    companies.insert_many(clean_data)

    return "Data is cleaned and put in the database"


if __name__ == '__main__':
    app.run()
