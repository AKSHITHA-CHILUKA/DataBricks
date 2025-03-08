# Databricks notebook source
spark.version

# COMMAND ----------

data=[("Alice",25),("Bob",30),("Charlie",35)]
df=spark.createDataFrame(data,["Name","Age"])
df.show()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

sc

# COMMAND ----------

myrdd1 = sc.parallelize([1,2,3,4,5,6,7,8,9,10])

# COMMAND ----------

myrdd1.collect()

# COMMAND ----------

myrdd2 = myrdd1.map(lambda x: x+10) #map 
myrdd2.collect() #action


# COMMAND ----------

# MAGIC %md
# MAGIC - myrdd3 = sc.textFile("")
# MAGIC - myrdd4 = myrdd3.flatMap(lambda line :line.split(" "))
# MAGIC - myrdd_pairs = rdd
