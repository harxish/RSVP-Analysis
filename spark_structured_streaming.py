from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *


spark = SparkSession.builder.appName("Stonks").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")


# # Type
# schema = StructType([
#     StructField("response", StringType()),
# ])

dumm = StructType([
      
      StructField("venue", StructType([
        StructField("venue_name", StringType()),
        StructField("lon", StringType()),
        StructField("lat", StringType()),
        StructField("venue_id", StringType())
      ]))])

schema = StructType([
      
      StructField("venue", StructType([
        StructField("venue_name", StringType()),
        StructField("lon", StringType()),
        StructField("lat", StringType()),
        StructField("venue_id", StringType())
      ])), 

      StructField("visibility", StringType()),
      StructField("response", StringType()),
      StructField("guests", StringType()),

      StructField("member", StructType([
        StructField("member_id", StringType()),
        StructField("photo", StringType()),
        StructField("member_name", StringType())
      ])),

      StructField("rsvp_id", StringType()),
      StructField("mtime", StringType()),

      StructField("event", StructType([
        StructField("event_name", StringType()),
        StructField("event_id", StringType()),
        StructField("time", StringType()),
        StructField("event_url", StringType())
      ])),

      StructField("group", StructType([
        StructField("group_topics", ArrayType(StructType([
          StructField("urlkey", StringType()),
          StructField("topic_name", StringType())
        ]))),


        StructField("group_city", StringType()),
        StructField("group_country", StringType()),
        StructField("group_id", StringType()),
        StructField("group_name", StringType()),
        StructField("group_lon", StringType()),
        StructField("group_urlname", StringType()),
        StructField("group_state", StringType()),
        StructField("group_lat", StringType())

      ]))

      ])


df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "meetup-rsvp") \
    .load()

df1 = df.selectExpr("CAST(value AS STRING)")
df1.printSchema()
df2 = df1.select(from_json(col("value"), dumm))
df2.printSchema()

df2.writeStream.format("console").option("truncate", "false") \
    .start().awaitTermination()

# query.pprint()
# query.start()
# query.awaitTermination()

# df = df.rdd.map(lambda x: x.json)
# df = spark.read.json(df)
# df = df.rdd.map(lambda x: (x, 1))
# df.printSchema()

# df.writeStream.format("console").option("truncate", "false") \
#     .start().awaitTermination()