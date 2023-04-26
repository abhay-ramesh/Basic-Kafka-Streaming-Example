import json
import requests
from time import sleep
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

for i in range(10):
    for i in range(5):
        # Mae a request to get the current location of the ISS
        res=requests.get('http://api.open-notify.org/iss-now.json')
        data = res.content.decode('utf-8')
        print(data)

        # Asynchronous by default
        future = producer.send('quickstart', bytes(str(data).encode('utf-8')))
    print("Sleeping for 5 seconds")
    sleep(5)

# block until all async messages are sent
producer.flush()

# configure multiple retries
producer = KafkaProducer(retries=5)