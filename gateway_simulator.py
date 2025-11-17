# gateway_simulator.py

import requests
import time
import random
from datetime import datetime

GATEWAY_ID = "GW-001"

def generate_meter_data():
    meters = []
    for i in range(1, 5):   # 4 meters for demo
        meters.append({
            "meter_id": f"M{i}",
            "flow": round(random.uniform(5.0, 20.0), 2),
            "status": "OK",
        })
    return meters

while True:
    payload = {
        "gateway_id": GATEWAY_ID,
        "meters": generate_meter_data(),
        "timestamp": datetime.now().isoformat()
    }

    try:
        r = requests.post("http://127.0.0.1:8000/data", json=payload)
        print("Gateway sent data:", r.status_code)
    except Exception as e:
        print("Error:", e)

    time.sleep(5)  # send every 5 seconds for demo
