# mi_script.py
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataprocJob").getOrCreate()

df = spark.createDataFrame([(1, 'Google'), (2, 'Cloud')], ["id", "name"])
df.show()

spark.stop()
