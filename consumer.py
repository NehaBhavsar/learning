from kafka import KafkaConsumer
import json

BOOTSTRAP_SERVERS = "localhost:9092"
TOPIC = "recommendItems"
GROUP_ID = "recommend-group"  # Consumer group ID

# Create a Kafka consumer
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    auto_offset_reset='earliest',  # start reading from earliest message
    enable_auto_commit=True,
    group_id=GROUP_ID,
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    key_deserializer=lambda k: k.decode('utf-8') if k else None
)

print(f"Consumer started, listening to topic '{TOPIC}'...\n")

try:
    for message in consumer:
        print(
            f"Received message: key={message.key}, "
            f"value={message.value}, "
            f"partition={message.partition}, "
            f"offset={message.offset}"
        )

except KeyboardInterrupt:
    print("Consumer stopped manually.")

finally:
    consumer.close()
