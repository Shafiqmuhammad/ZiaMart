from confluent_kafka import Consumer

def get_kafka_consumer(group_id: str, topics: list):
    consumer_config = {
        'bootstrap.servers': 'kafka:9092',
        'group.id': group_id,
        'auto.offset.reset': 'earliest',
    }

    try:
        consumer = Consumer(consumer_config)
        consumer.subscribe(topics)
        return consumer
    except Exception as e:
        print(f"Error creating Kafka consumer: {e}")
        raise
