from kafka import KafkaConsumer
import csv
import json

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('quickstart',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'])

print("Consumer is ready to consume messages")

# with open('test.csv', 'w') as csvfile:
#     fieldnames = ['topic', 'partition', 'offset', 'key', 'latitude', 'longitude', 'message', 'timestamp']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
with open('data.csv', 'w') as csvfile:
    fieldnames = ['topic', 'partition', 'offset', 'key', 'latitude', 'longitude', 'message', 'timestamp']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    

for message in consumer:
    print("Message consumed")
    with open('data.csv', 'a') as csvfile:
        fieldnames = ['topic', 'partition', 'offset', 'key', 'latitude', 'longitude', 'message', 'timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                message.offset, message.key,
                                                message.value))
        data = json.loads(message.value)
        print(data['iss_position']['latitude'])
        writer.writerow({'topic': message.topic, 'partition': message.partition, 'offset': message.offset, 'key': message.key, 'latitude': data['iss_position']['latitude'], 'longitude': data['iss_position']['longitude'], 'message': data['message'], 'timestamp': data['timestamp']})
        print("Message written to csv file")
        