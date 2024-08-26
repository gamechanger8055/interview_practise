from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send a message with a key (this will go to the same partition)
producer.send('my-topic', key=b'my-key', value=b'Hello, Kafka!')

# Send a message without a key (this will be round-robin or based on default partitioner)
producer.send('my-topic', value=b'Hello, Kafka!')

producer.flush()

from kafka import KafkaConsumer

consumer = KafkaConsumer('my-topic', group_id='my-group', bootstrap_servers='localhost:9092')

for message in consumer:
    print(f"Partition: {message.partition}, Offset: {message.offset}, Key: {message.key}, Value: {message.value}")
