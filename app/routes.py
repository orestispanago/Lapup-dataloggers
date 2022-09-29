from sys import stdout
from flask import request, jsonify
import mysql.connector
from __main__ import app

config = {
    "user": "root",
    "password": "root",
    "host": "172.20.0.2",
    "port": "3306",
    "database": "collector",
}


@app.route("/last", methods=["GET"])
def last():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        f"SELECT * FROM `collector`.`measurements` ORDER BY id DESC LIMIT 1;"
    )
    results = cursor.fetchone()
    cursor.close()
    connection.close()
    return jsonify(results)


@app.route("/store", methods=["POST"])
def measurement():
    data = request.json
    records = data["records"]
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    col_names = ",".join(records[0].keys())
    for rec in records:
        sql = f"INSERT INTO measurements ({col_names}) VALUES (%s, %s)"
        val = (rec["time"], rec["temp_in"])
        cursor.execute(sql, val)
        connection.commit()
    cursor.close()
    connection.close()
    return "SUCCESS"
