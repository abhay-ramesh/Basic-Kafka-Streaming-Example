# Kafka Streaming Basic Example

## Description

This is a basic example of Kafka Streaming using Python. The example is based on the [Kafka Streaming Tutorial](https://kafka.apache.org/10/documentation/streams/tutorial) from the official Kafka documentation.

## Requirements

* Python 3.6

## Installation

1. Clone the repository
2. Run `pip install -r requirements.txt` to install the dependencies
3. cd into kafka and run `docker-compose up -d` to start the Kafka cluster
4. cd into mysql and run `docker-compose up -d` to start the MySQL database
5. run `python create_table.py` to create the table in the database
6. run `python producer.py` to start the producer
7. run `python consumer2.py` to start the consumer (in a new terminal) which will average the data of the last 10 seconds and write it to the database
8. Now the database can be queried to get the average price in 10 second intervals

## Authors

* [**Abhay Ramesh**](https://github.com/abhay-ramesh)
