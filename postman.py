import requests
import datetime


def get_last_record():
    get_resp = requests.get("http://localhost:5000/last/meteo")
    # print("GET status:", get_resp.status_code)
    # print(get_resp.text)
    data = get_resp.json()
    last_record = datetime.datetime.strptime(
        data["Datetime"], "%a, %d %b %Y %H:%M:%S GMT"
    )
    print("Last record:", last_record)
    return last_record


def populate_db(million_rows=61):
    for m in range(million_rows):
        print(m)
        last_rec = get_last_record()
        payload = {
            "records": [
                {
                    "Datetime": str(last_rec + datetime.timedelta(seconds=i * 10)),
                    "temp": i,
                    "RH": i,
                    "press": i,
                }
                for i in range(1, 1_000_001)
            ]
        }
        resp = requests.post("http://localhost:5000/store/meteo", json=payload)

        print("POST status:", resp.status_code)
        print(resp.text)


# populate_db(million_rows=61)
date_range = {"start_date": "2000-01-01 00:00:00", "end_date": "2000-12-01 00:00:00"}
get_resp = requests.post("http://localhost:5000/range/meteo", json=date_range)

print("POST status:", get_resp.status_code)
# print(get_resp.text)

# get_resp = requests.get("http://localhost:5000/last/meteo")
# print(get_resp.status_code)
# print(get_resp.text)
