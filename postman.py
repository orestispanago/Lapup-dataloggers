import requests

url = "http://localhost:5000/measurement"
myobj = {"somekey": 100}

resp = requests.post(url, json=myobj)

print("Status:", resp.status_code)
print(resp.text)
