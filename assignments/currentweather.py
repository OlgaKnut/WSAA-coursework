import json
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=52.25&longitude=-9.73&current=temperature_2m,wind_direction_10m"
response = requests.get (url)
data = (response.json())
current_units = data["current_units"]
temp_units = current_units["temperature_2m"]
wind_dir_units = current_units["wind_direction_10m"]
current = data["current"]
temperature = current["temperature_2m"]
wind_direction = current["wind_direction_10m"]
print("Current weather in Tralee: temperature",temperature,temp_units, 
      ", wind direction", wind_direction, wind_dir_units)

