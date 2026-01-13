# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT 
# MAGIC   date,
# MAGIC   temperature_max,
# MAGIC   temperature_min,
# MAGIC   precipitation_probability
# MAGIC FROM `samples`.`accuweather`.`forecast_daily_calendar_imperial`
# MAGIC WHERE temperature_max > 75
# MAGIC ORDER BY date DESC;
