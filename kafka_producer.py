import websocket
import json

from kafka import KafkaProducer

KAFKA_PRODUCER = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('utf-8'),
                               bootstrap_servers=['localhost:9092'])

def on_message(wsapp, message):
    print(message)
    KAFKA_PRODUCER.send('meetup-rsvp', message)
    KAFKA_PRODUCER.flush()

def on_error(wsapp, error):
    print(error)

def on_close(wsapp):
    print("Connection Closed")

def main():
    websocket.enableTrace(True)
    print("Connection Established")
    wsapp = websocket.WebSocketApp("wss://stream.meetup.com/2/rsvps", 
                                    on_message=on_message, 
                                    on_error=on_error,
                                    on_close=on_close)
    wsapp.run_forever()

if __name__ == '__main__':
    main()