import json
from sqlmodel import select
from users.db import async_session
from confluent_kafka import Consumer  # Ensure this import is present

# Function to initialize Kafka consumer
def get_kafka_consumer(group_id: str, topics: list):
    consumer_config = {
        'bootstrap.servers': 'broker:19092',  # Ensure 'broker' matches your Kafka broker container name
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

# Function to consume messages from Kafka and insert into the database
async def consume_message_request():
    consumer = get_kafka_consumer("ugroup1", ["topic1"])
    try:
        # Poll for messages
        msg = consumer.poll(3.0)  # Polls for messages with a 1 second timeout
        if msg is None:
            return

        if msg.error():
            print(f"Kafka error: {msg.error()}")
            return

        # Assuming the message contains user registration data in JSON format
        user_data = json.loads(msg.value().decode('utf-8'))

        # Process and insert into the database asynchronously
        async with async_session() as session:
            # Check if the user already exists
            result = await session.exec(select(User).where(User.email == user_data["email"]))
            existing_user = result.first()
            
            if existing_user:
                print(f"User with email {user_data['email']} already exists.")
                return

            # Insert the new user
            new_user = User(username=user_data["username"], email=user_data["email"], password=user_data["password"])
            session.add(new_user)
            await session.commit()  # Commit the transaction
            print(f"User {user_data['email']} registered successfully.")
    
    except Exception as e:
        print(f"Error processing message: {e}")

    await asyncio.sleep(10)  # Short delay before checking for the next message