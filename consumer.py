from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers='192.168.99.100:9092', auto_offset_reset='earliest')

consumer.subscribe(['MyTopic1', 'MyTopic2'])

for msg in consumer:
    print("Key: " + str(msg.key) + ", value: " + str(msg.value) + " in topic: " + str(msg.topic))
