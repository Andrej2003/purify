import sqlite3
import pymongo
from flask import Flask

app = Flask(__name__)


@app.route('/data', methods=["GET"])
def read_data():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM companies")
    data = cursor.fetchall()
    return data


# @app.route('/write_data', methods=["POST"])
# def write_data():
#     client = pymongo.MongoClient("mongodb://localhost:27017")
#     db = client['purified_data']


if __name__ == '__main__':
    app.run()
