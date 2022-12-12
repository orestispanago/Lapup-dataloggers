import datetime

import requests


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
        resp = requests.post(
            f"http://localhost:5000/store/{table}", json=payload
        )

        print("POST status:", resp.status_code)
        print(resp.text)


# populate_db(hundrend_thousand_rows=270)
# date_range = {
#     "start_date": "2015-05-02 00:00:00",
#     "end_date": "2016-05-02 23:59:00",
# }
payload = {
    "records": [
        {
            "Datetime_UTC": str(datetime.datetime.utcnow()),
            "UV_301nm": 611.0,
            "UV_312nm": 39090.0,
            "UV_320nm": 35860.0,
            "UV_340nm": 71280.0,
            "UV_380nm": 14620.0,
            "PAR": 59270.0,
            "temp_int_C": 50.0,
        }
    ]
}

get_resp = requests.post(
    "http://snf-882758.vm.okeanos.grnet.gr:5000/store/nilu", json=payload
)

print("POST status:", get_resp.status_code)
print(get_resp.text)
