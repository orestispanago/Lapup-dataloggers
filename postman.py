import requests
import datetime


def get_last_record(table="meteo1min"):
    get_resp = requests.get(f"http://localhost:5000/last/{table}")
    # print("GET status:", get_resp.status_code)
    # print(get_resp.text)
    data = get_resp.json()
    last_record = datetime.datetime.strptime(
        data["Datetime"], "%a, %d %b %Y %H:%M:%S GMT"
    )
    print("Last record:", last_record)
    return last_record


def populate_db(hundrend_thousand_rows=5, table="meteo1min"):
    for m in range(hundrend_thousand_rows):
        print(m)
        last_rec = get_last_record(table=table)
        payload = {
            "records": [
                {
                    "Datetime": str(last_rec + datetime.timedelta(minutes=i)),
                    "temp": i,
                    "RH": i,
                    "press": i,
                    "ws": i,
                    "wd": i,
                    "prec": i,
                    "rain": i,
                    "bat": i,
                }
                for i in range(1, 100_001)
            ]
        }
        resp = requests.post(f"http://localhost:5000/store/{table}", json=payload)

        print("POST status:", resp.status_code)
        print(resp.text)


# populate_db(hundrend_thousand_rows=270)
date_range = {"start_date": "2015-05-02 00:00:00", "end_date": "2016-05-02 23:59:00"}
get_resp = requests.post("http://localhost:5000/range/meteo1min", json=date_range)

print("POST status:", get_resp.status_code)
print(len(get_resp.json()))

# get_resp = requests.get("http://localhost:5000/last/meteo1min")
# print(get_resp.status_code)
# print(get_resp.text)
