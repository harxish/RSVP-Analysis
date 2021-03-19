# Meetup RSVP Stream Analysis

## Abstract

Meetup is a service used to organize online groups that host in-person and virtual events for people with similar interests. It provides an API which gives us real time RSVP to these events. We try to solve two problems in here,

- Allow meetup organizers to identify trending topics related to their meetup. We computed Trending Topics based on the description of the events matching the tags of interest to us.
- See which Meetup events attract the most responses within our region.
<br><br>

## Big Data Architecture


![](images/image1.png)
<br><br><br>

## Technology Stack

- [WebSocket](https://websocket-client.readthedocs.io/en/latest/index.html) - Library used to read JSON response from meetup website.
<br><br>

## Prerequisites

- Apache Kafka
- Apache Spark
<br><br>

## How to install

``$> pipenv install --ignore-pipfile``
<br>or<br>
``$> pip install -r requirements.txt``
<br><br>

## How to Run

```
./bin/zookeeper-server-start.sh config/zookeeper.properties
./bin/kafka-server-start.sh config/server.properties

pipenv run python3 kafka_producer.py
```

```
/opt/spark/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.0 spark_streaming_kafka.py
```