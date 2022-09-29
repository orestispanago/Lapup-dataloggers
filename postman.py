import requests
import datetime

url = "http://localhost:5000/store"

payload = {
    "records": [
        {"time": str(datetime.datetime.utcnow()), "temp_in": 3},
        {"time": str(datetime.datetime.utcnow()), "temp_in": 30},
        {"time": str(datetime.datetime.utcnow()), "temp_in": 100},
    ]
}

resp = requests.post(url, json=payload)

print("POST status:", resp.status_code)
print(resp.text)


get_resp = requests.get("http://localhost:5000/last")

print("GET status:", get_resp.status_code)
print(get_resp.text)
