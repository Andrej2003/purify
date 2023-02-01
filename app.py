import sqlite3
import pymongo
import json
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path="/static")


@app.route('/')
@app.route('/companies-data', methods=["GET"])
def read_data():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM companies")
    data = cursor.fetchall()
    column_names = [name[0] for name in cursor.description]
    return [data, column_names]


@app.route('/')
@app.route('/companies-data', methods=["GET"])
def read_data_template():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM companies")
    data = cursor.fetchall()
    column_names = [name[0] for name in cursor.description]
    return render_template("index.html", data=data, columns=column_names)


@app.route('/companies-data/purify', methods=["POST"])
def write_data():
    clean_data = json.loads(request.json)

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['purified_data']
    companies = db["companies"]
    companies.insert_many(clean_data)

    return "Data is cleaned and put in the database"


if __name__ == '__main__':
    app.run()
