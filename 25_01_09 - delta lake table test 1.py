# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE table employees (id Int, name string, salary double)

# COMMAND ----------

# MAGIC %sql
# MAGIC Insert into employees values (2, "mingyao xiao2", 100002), (3, "mingyao xiao3", 100003), (4, "mingyao xiao4", 100004), (5, "mingyao xiao5", 100005), (6, "mingyao xiao6", 100006)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from mx_test_sandbox_db.default.employees

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail employees

# COMMAND ----------

# MAGIC %sql
# MAGIC Describe history employees
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employees version as of 2

# COMMAND ----------

# MAGIC %sql
# MAGIC Describe extended employees

# COMMAND ----------

print("25_02_17 - Hi")

# COMMAND ----------

print("25_02_17_1843 - Hi again")
