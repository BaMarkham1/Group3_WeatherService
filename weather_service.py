# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:15:12 2020

@author: lemar
"""
import json
import weather_grabber as wg

#set the zip code you want here
zip_code = "67735"
#set the type of forecast you want
#valid types: currently, daily, hourly, and alerts
forecast_type = "alerts"
#call the weather_grabber module's get_weather function
data = wg.get_weather(zip_code, forecast_type)
#this is a default way to print a json in an organized fashion
#this can be changed to send a message to the user in the way we want
print(json.dumps(data, indent=2))

