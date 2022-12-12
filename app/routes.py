import MySQLdb
from __main__ import app
from flask import jsonify, request

config = {
    "user": "root",
    "password": "root",
    "host": "172.20.0.2",
    "port": 3306,
    "database": "lapupdb",
}


@app.route("/last", methods=["GET"])
def last_records():
    connection = MySQLdb.connect(**config)
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f"SELECT * FROM last_records;")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(results)


@app.route("/last/<tablename>", methods=["GET"])
def last_record(tablename):
    connection = MySQLdb.connect(**config)
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f"SELECT * FROM {tablename} ORDER BY id DESC LIMIT 1;")
    results = cursor.fetchone()
    cursor.close()
    connection.close()
    return jsonify(results)


def prepare_update_statement(records, table=None):
    last_record_time = records[-1]["Datetime_UTC"]
    return (
        f"UPDATE last_records "
        f"SET last_record_utc = '{last_record_time}'"
        f"WHERE table_name = '{table}';"
    )


def prepare_insert_statement(records, table=None):
    columns = ", ".join(records[0].keys())
    val_list = [tuple(r.values()) for r in records]
    values = ", ".join(map(str, val_list))
    return f"""INSERT INTO {table} ({columns}) VALUES {values};"""


@app.route("/store/<tablename>", methods=["POST"])
def store_records(tablename):
    data = request.json
    records = data["records"]
    insert_statement = prepare_insert_statement(records, table=tablename)
    update_statement = prepare_update_statement(records, table=tablename)
    connection = MySQLdb.connect(**config)
    cursor = connection.cursor()
    cursor.execute(insert_statement)
    cursor.execute(update_statement)
    connection.commit()
    cursor.close()
    connection.close()
    return "OK"


@app.route("/range/<tablename>", methods=["POST"])
def get_time_range(tablename):
    data = request.json
    start_date = data["start_date"]
    end_date = data["end_date"]
    connection = MySQLdb.connect(**config)
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        f"""SELECT * FROM {tablename} WHERE `Datetime` BETWEEN '{start_date}' AND '{end_date}';"""
    )
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(results)
