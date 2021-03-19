from kafka import KafkaConsumer
import json


consumer = KafkaConsumer('meetup-rsvp',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

print("consumer started ...")

for message in consumer:
    data = str(message.value)
    print("Sending: ", data)