# Databricks notebook source
print('Welcome') 
import numpy np

# COMMAND ----------

List = [1,2,4,5]

# COMMAND ----------

# MAGIC %md
# MAGIC # Title 1
# MAGIC ## Title 2
# MAGIC ### Title 3
# MAGIC Order
# MAGIC 1.y

# COMMAND ----------

# MAGIC %run ./Includes/Setup

# COMMAND ----------

print(full_name)



# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)
display(files)

# COMMAND ----------


