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
    col_names = records[0].keys()
    values_placeholders = ", ".join(["%s"] * len(col_names))
    col_names_placeholders = ", ".join(col_names)
    for rec in records:
        insert_query = """ INSERT INTO measurements (%s) VALUES (%s) """ % (
            col_names_placeholders,
            values_placeholders,
        )
        val = list(rec.values())
        cursor.execute(insert_query, val)
        connection.commit()
    cursor.close()
    connection.close()
    return "SUCCESS"
