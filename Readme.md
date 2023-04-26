# Kafka Streaming Basic Example

## Description

This is a basic example of Kafka Streaming using Python. The example is based on the [Kafka Streaming Tutorial](https://kafka.apache.org/10/documentation/streams/tutorial) from the official Kafka documentation.

## Requirements

* Python 3.6

## Installation

1. Clone the repository
2. Run `pip install -r requirements.txt` to install the dependencies
3. cd into kafka and run `docker-compose up -d` to start the Kafka cluster
4. run `python producer.py` to start the producer
5. run `python consumer.py` to start the consumer
6. Now the data is streamed from the producer to the consumer and written to `data.csv`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Authors

* [**Abhay Ramesh**](https://github.com/abhay-ramesh)
