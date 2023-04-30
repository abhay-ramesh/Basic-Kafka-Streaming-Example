# Start the apache consumer and for every 10 seconds of data use spark to calculate the average price of bitcoin and send it to mysql database.
#
# Path: spark.py

# from pyspark.sql.functions import *
# from pyspark.sql.types import *
# from pyspark.sql import SparkSession
import mysql.connector
from kafka import KafkaConsumer
import csv
import json
import requests
import time


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

# For every 10 seconds of data save it to csv file untill 5 minutes keep it in loop
starttime = time.time()
while (time.time() - starttime) < 300:

    chunkdata = []

    for message in consumer:
        print("Message consumed")
        data = json.loads(message.value)
        chunkdata.append(data)
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                message.offset, message.key,
                                                data))
        print("Message written to csv file")
        if time.time() - starttime > 10:
            print("10 seconds of data is collected")
            print("Calculating average price of bitcoin")
            avgprice = sum([float(i['data']['rateUsd']) for i in chunkdata])/len(chunkdata)
            print("Average price of bitcoin is %s" % avgprice)
            print("Sending average price of bitcoin to mysql database")
            mycursor = mydb.cursor()
            sql = "INSERT INTO bitcoin (price) VALUES (%s)"
            val = (avgprice,)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Average price of bitcoin is sent to mysql database")
            chunkdata = []
            starttime = time.time()
            break
        break


            