from flask import request, jsonify
import mysql.connector
from __main__ import app

config = {
    "user": "root",
    "password": "root",
    "host": "172.20.0.2",
    "port": "3306",
    "database": "lapup",
}


@app.route("/last/<tablename>", methods=["GET"])
def last(tablename):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {tablename} ORDER BY id DESC LIMIT 1;")
    results = cursor.fetchone()
    cursor.close()
    connection.close()
    return jsonify(results)


def prepare_insert_statement(records, table=None):
    columns = ", ".join(records[0].keys())
    val_list = [tuple(r.values()) for r in records]
    values = ", ".join(map(str, val_list))
    return f"""INSERT INTO {table} ({columns}) VALUES {values};"""


@app.route("/store/<tablename>", methods=["POST"])
def store_records(tablename):
    data = request.json
    records = data["records"]
    query = prepare_insert_statement(records, table=tablename)
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    return "OK"


@app.route("/range/<tablename>", methods=["POST"])
def get_time_range(tablename):
    data = request.json
    start_date = data["start_date"]
    end_date = data["end_date"]
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        f"""SELECT * FROM {tablename} WHERE `Datetime` BETWEEN '{start_date}' AND '{end_date}';"""
    )
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(results)
