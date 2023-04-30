import json
import requests
import time
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

startTime=time.time()

while (time.time()-startTime)<300:
    # Make a request to get the current location of the ISS
    res=requests.get('https://api.coincap.io/v2/rates/bitcoin')
    data = res.content.decode('utf-8')
    print(data)

    # Asynchronous by default
    future = producer.send('quickstart', (str(data).encode('utf-8')))
    # print("Sleeping for 1 seconds")
    print("Ran for %s seconds" % (time.time()-startTime))
    time.sleep(1)

# block until all async messages are sent
producer.flush()

# configure multiple retries
producer = KafkaProducer(retries=5)