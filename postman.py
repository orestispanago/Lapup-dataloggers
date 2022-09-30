import requests
import datetime

payload = {
    "records": [
        {"time": str(datetime.datetime.utcnow()), "temp_in": i} for i in range(100000)
    ]
}

resp = requests.post("http://localhost:5000/store", json=payload)

print("POST status:", resp.status_code)
print(resp.text)


get_resp = requests.get("http://localhost:5000/last")

print("GET status:", get_resp.status_code)
print(get_resp.text)
