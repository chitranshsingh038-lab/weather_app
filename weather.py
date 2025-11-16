
import requests
import json
import time

t=time.localtime()
current_time = time.strftime("%H:%M", t)

city_name = input("Enter city name: ")
api_key = input("enter you api key :")

api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

response = requests.get(api_url)
data=response.json()
data2=json.dumps(data, indent=4)

# error handling(wrong city,wrong api key,etc)
if(response.status_code != 200):
    print("Error fetching data from the API. Please check the city name and API key.")
    exit()
else:    
    d=data["weather"][0]
    
    #for only curly brackets we don't need to use [0]
    tem=data["main"]["temp"]
    print(f"temperature in {city_name} at {current_time} is {tem}°C")