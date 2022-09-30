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


def prepare_insert_statement(records):
    columns = ", ".join(records[0].keys())
    val_list = [tuple(r.values()) for r in records]
    values = ", ".join(map(str, val_list))
    return f"""INSERT INTO measurements ({columns}) VALUES {values};"""


@app.route("/store", methods=["POST"])
def measurement():
    data = request.json
    records = data["records"]
    query = prepare_insert_statement(records)
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    return "SUCCESS"
