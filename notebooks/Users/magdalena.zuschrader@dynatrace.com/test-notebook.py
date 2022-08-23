# Databricks notebook source
import os

output = os.popen('ping -c 5 github.com')

while True:
  line = output.readline()
  
  if line:
    print(line)
  else:
    break

output.close()

# COMMAND ----------

print("Hello world!")

# COMMAND ----------

