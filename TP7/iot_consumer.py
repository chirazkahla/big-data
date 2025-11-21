from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'machines',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Listening for IoT data...\n")

for msg in consumer:
    data = msg.value
    print("Received:", data)

    if data["temperature"] > 80:
        print("🔥 Warning: High temperature detected!")

    if data["vibration"] > 1.5:
        print("⚠️ Alert: High vibration detected!")
