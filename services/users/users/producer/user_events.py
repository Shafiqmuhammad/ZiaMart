from confluent_kafka import Producer
from users.protobuf.user_pb2 import UserCreatedEvent

class UserEvents:
    def __init__(self):
        self.producer = Producer({'bootstrap.servers': 'kafka:9092'})

    def produce_user_created_event(self, user_data):
        event = UserCreatedEvent(user=user_data)
        serialized_event = event.SerializeToString()
        try:
            self.producer.produce('user-topic', value=serialized_event)
            self.producer.flush()
        except Exception as e:
            print(f"Error producing Kafka event: {e}")
