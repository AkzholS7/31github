#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

#before running the script please install the kafka using this command: pip install confluent-kafka
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Producer, Consumer, KafkaError

bootstrap_servers = 'localhost:9092'
topic_name = 'test_topic'

def create_topic():
    admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})
    topic = NewTopic(topic_name, num_partitions=3, replication_factor=1)
    fs = admin_client.create_topics([topic])

    for topic, f in fs.items():
        try:
            f.result()
            print(f"Topic {topic} created")
        except Exception as e:
            print(f"Failed to create topic {topic}: {e}")

def produce_messages():
    p = Producer({'bootstrap.servers': bootstrap_servers})

    try:
        for i in range(5):
            p.produce(topic_name, f"Message {i}")
            p.poll(0.5)

        print("Messages produced successfully")
    except Exception as e:
        print(f"Failed to produce messages: {e}")
    finally:
        p.flush()

def consume_messages():
    c = Consumer({
        'bootstrap.servers': bootstrap_servers,
        'group.id': 'my-group',
        'auto.offset.reset': 'earliest'
    })

    c.subscribe([topic_name])

    try:
        while True:
            msg = c.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print("End of partition reached")
                    break
                else:
                    print(f"Error: {msg.error()}")
                    break

            print(f"Received message: {msg.value().decode('utf-8')}")

    except KeyboardInterrupt:
        pass
    finally:
        c.close()

if __name__ == '__main__':
    print("Kafka Python Script")
    print("1. Create Topic")
    print("2. Produce Messages")
    print("3. Consume Messages")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_topic()
    elif choice == '2':
        produce_messages()
    elif choice == '3':
        consume_messages()
    elif choice == '4':
        print("Exiting the script")
    else:
        print("Invalid choice. Exiting.")