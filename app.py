import sqlite3
import pymongo
from flask import Flask

app = Flask(__name__)


@app.route('/<company_id>', methods=["GET"])
def read_data(company_id):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM companies WHERE id={company_id}")
    data = list(cursor.fetchone())
    return data


# @app.route('/write_data', methods=["POST"])
# def write_data():
#     client = pymongo.MongoClient("mongodb://localhost:27017")
#     db = client['purified_data']


if __name__ == '__main__':
    app.run()
