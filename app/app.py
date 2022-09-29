from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json

app = Flask(__name__)


@app.route("/measurement", methods=["GET", "POST"])
def measurement():
    config = {
        "user": "root",
        "password": "root",
        "host": "172.20.0.2",
        "port": "3306",
        "database": "collector",
    }
    if request.method == "GET":
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM `collector`.`measurements`;")
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return str(results)
    if request.method == "POST":
        data = request.json
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        sql = f"INSERT INTO measurements (temp_in) VALUES ({data['somekey']})"
        cursor.execute(sql)
        cursor.close()
        connection.commit()
        connection.close()
        return "SUCCESS"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
