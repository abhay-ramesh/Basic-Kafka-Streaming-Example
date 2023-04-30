# Initialize mysql database and create table bitcoin:

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
     user="root",
    passwd="password",
    database="dbt"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE bitcoin (price VARCHAR(255))")

# Run the following commands in the terminal to start the producer, consumer and spark streaming:
# python producer.py
# python consumer.py