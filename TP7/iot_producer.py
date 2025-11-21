from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "machine_id": "M1",
        "temperature": round(random.uniform(40, 100), 2),
        "vibration": round(random.uniform(0.5, 2.0), 2),
        "timestamp": str(datetime.now())
    }

    producer.send('machines', data)
    print("Data sent:", data)
    time.sleep(1)
