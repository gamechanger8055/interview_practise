from confluent_kafka import Producer,Consumer,TopicPartition
# Set the connection properties
conf = {
'bootstrap.servers': 'kafka-broker:9092',
'client.id': 'my-client-id',
'enable.idempotence': True, # Enable idempotence for guaranteed message delivery
'linger.ms': 1000, # Wait up to 1 second to batch messages for better throughput
'max.in.flight.requests.per.connection': 5, # Control the number of in-flight requests per connection
'connections.max.idle.ms': 5 * 60 * 1000 # Keep connections open for up to 5 minutes
}
# Create a Kafka producer with the connection properties
producer = Producer(conf)
# Send a message to a topic
producer.produce(topic='my-topic', value='Hello, world!')
# Flush the producer to ensure all messages are sent
producer.flush()
# Close the producer to release resources
producer.close()
consumer=Consumer(conf)
consumer.consume(5)