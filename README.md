# Meetup RSVP Stream Analysis

## Abstract

Meetup is a service used to organize online groups that host in-person and virtual events for people with similar interests. It provides an API which gives us real time RSVP to these events. We try to solve two problems in here,

- Allow meetup organizers to identify trending topics related to their meetup. We computed Trending Topics based on the description of the events matching the tags of interest to us.
- See which Meetup events attract the most responses within our region.
- Plot the grouped records.
<br><br>

## Big Data Architecture


![](images/image1.png)
<br><br><br>

## Technology Stack

- [WebSocket](https://websocket-client.readthedocs.io/en/latest/index.html) - Library used to read JSON response from meetup website.
- [Kafka](https://kafka.apache.org/) - Used to collect the responses from the WebSocket module and add it to the meetup-rsvp topic.
- [Spark Streaming](https://spark.apache.org/streaming/) - Used to Stream data from the Kafka Topic
- [Amazon RDS](https://aws.amazon.com/rds/) - Store the streaming processed data to plot.
- [Matplotlib](https://matplotlib.org/) - Plot the processed data from RDS.
<br><br>

## How to Run

1. Run the core ipynb to start the listening, process and upload it to the RDS server.
2. Run the plot ipynb to read data from RDS and plot it using matplotlib.
<br><br>

## Issues

Open an issue if you get any problem working with it :)
