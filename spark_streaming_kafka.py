import json
import findspark
import pandas as pd

findspark.add_packages(['org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.0'])
findspark.init()

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

def aggregate(_, x):
    x = x.collect()
    # for i in x:
    #     countries.loc[countries['alpha-2'] == i[0], ['count']] += i[1]
    print(x)

countries = pd.read_csv('./all.csv')
countries = countries[['name', 'alpha-2', 'region']]
countries = countries.dropna()
countries['alpha-2'] = countries['alpha-2'].str.lower()
countries.loc[countries['alpha-2'] == 'gb', ['name']] = 'Britain'
countries['count'] = 0    

sc = SparkContext(appName='Demo')
ssc = StreamingContext(sc, 2)

sc.setLogLevel("ERROR")

brokers, topic = 'localhost:9092', 'meetup-rsvp'
raw_data = KafkaUtils.createDirectStream(ssc, [topic], {'metadata.broker.list': brokers})

stream_data = raw_data.map(lambda x: json.loads(x[1])).map(lambda x: json.loads(x))
stream_data = stream_data.flatMap(lambda x: x.items())

group_country = stream_data.filter(lambda x: x[0] == 'group')
group_country = group_country.map(lambda x: x[1]['group_country'])
group_country = group_country.map(lambda x: (x, 1))
group_country = group_country.reduceByKey(lambda a, b: a+b).foreachRDD(aggregate)

ssc.start()
ssc.awaitTermination(timeout=15)
ssc.stop()
sc.stop()

print(countries)