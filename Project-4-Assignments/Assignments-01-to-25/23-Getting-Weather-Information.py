import requests
from pprint import pprint

API_KEY = "2c79324eda9fc48dc439aba7e28535bd"

city = input("Enter a city: ")

base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

weather_data = requests.get(base_url).json()

pprint(weather_data)