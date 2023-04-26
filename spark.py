import findspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json 
import time
findspark.init()

if __name__=="__main__":
    
    spark=SparkSession.builder.master("local").appName("Kafka Spark Demo").getOrCreate()
    
    sc=spark.sparkContext
    
    ssc=StreamingContext(sc,20)
    
    message=KafkaUtils.createDirectStream(ssc,topics=['quickstart'],kafkaParams={"metadata.broker.list": "localhost:9092"})
    
    
    data=message.map(lambda x: x[1])
    
    def functordd(rdd):
        try:
            rdd1=rdd.map(lambda x: json.loads(x))
            df=spark.read.json(rdd1)
            df.show()
            df.createOrReplaceTempView("Test")
            df1=spark.sql("select iss_position.latitude,iss_position.longitude,message,timestamp from Test")
            
            df1.write.format('csv').mode('append').save("testing")
            
        except:
            pass
    
    data.foreachRDD(functordd)