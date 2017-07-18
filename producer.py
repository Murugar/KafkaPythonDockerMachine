from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='192.168.99.100:9092')

producer.send('MyTopic1', b"first message")
producer.send('MyTopic2', b"second message")
