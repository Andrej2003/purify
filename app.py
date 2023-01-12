import sqlite3
import pymongo
from flask import Flask, request

app = Flask(__name__)


@app.route('/companies-data', methods=["GET"])
def read_data():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM companies")
    data = list(cursor.fetchone())
    return data


@app.route('/companies-data/purify', methods=["POST"])
def write_data():
    company_id = request.form.get("id")
    print(company_id)
    name = request.form.get("name")
    country_iso = request.form.get("country_iso")
    city = request.form.get("city")
    nace = request.form.get("nace")
    website = request.form.get("website")

    clean_data = {"id": company_id,
                  "name": name,
                  "country_iso": country_iso,
                  "city": city,
                  "nace": nace,
                  "website": website, }

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['purified_data']
    companies = db["companies"]
    companies.insert_one(clean_data)
    return "Data is cleaned and put in the database"


if __name__ == '__main__':
    app.run()
