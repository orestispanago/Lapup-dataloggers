import requests
import datetime

for r in range(3):
    payload = {
        "records": [
            {
                "Datetime": str(datetime.datetime.utcnow()),
                "temp": i,
                "RH": i,
                "press": i,
            }
            for i in range(1_000_000)
        ]
    }

    resp = requests.post("http://localhost:5000/store/meteo", json=payload)

    print("POST status:", resp.status_code)
    print(resp.text)


get_resp = requests.get("http://localhost:5000/last/meteo")

print("GET status:", get_resp.status_code)
print(get_resp.text)

date_range = {"start_date": "2022-09-30 11:04:00", "end_date": "2022-09-30 11:05:00"}
get_resp = requests.post("http://localhost:5000/range/meteo", json=date_range)

print("POST status:", get_resp.status_code)
print(get_resp.text)
