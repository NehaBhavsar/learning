from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import time

BOOTSTRAP_SERVERS = "localhost:9092"
TOPIC = "recommendItems"

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    key_serializer=lambda k: k.encode("utf-8") if k else None,
    acks="all",
    retries=3,
)

try:
    for i in range(10):
        message = {
            "id": i,
            "message": f"viewed item {i}"
        }

        future = producer.send(
            topic=TOPIC,
            key=str(i),
            value=message
        )

        # Block until send succeeds or fails
        record_metadata = future.get(timeout=10)

        print(
            f"Sent to topic={record_metadata.topic}, "
            f"partition={record_metadata.partition}, "
            f"offset={record_metadata.offset}"
        )

        time.sleep(1)

except KafkaError as e:
    print(f"Kafka error: {e}")

finally:
    producer.flush()
    producer.close()
