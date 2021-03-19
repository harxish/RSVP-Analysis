from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc = SparkContext(appName='Demo')
ssc = StreamingContext(sc, 2)

brokers, topic = 'localhost:9092', 'meetup-rsvp'
kvs = KafkaUtils.createDirectStream(ssc, [topic], {'metadata.broker.list': brokers})
# meetups = kvs.map(lambda x: eval(x[1]))

kvs.pprint()
ssc.start()
ssc.awaitTermination()