from kafka import KafkaConsumer
import csv
import json
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="dbt"
)

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('quickstart',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'])

print("Consumer is ready to consume messages")

with open('data.csv', 'w') as csvfile:
    fieldnames = ['topic', 'partition', 'offset', 'key', 'data']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
for message in consumer:
    print("Message consumed")
    with open('data.csv', 'a') as csvfile:
        fieldnames = ['topic', 'partition', 'offset', 'key', 'data']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        data = json.loads(message.value)
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                message.offset, message.key,
                                                data))
        writer.writerow({'topic': message.topic, 'partition': message.partition, 'offset': message.offset, 'key': message.key, 'data':data})
        print("Message written to csv file")
        