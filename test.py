import requests
import pprint
import json
import os

from dotenv import load_dotenv
from exсeptions import MissingEnvVaribleError   

load_dotenv()

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise MissingEnvVaribleError('Set API_KEY env varible in .env file')

while True:
    city = input("Чтобы выбрать город напишите его. Чтобы выйти напишите Stop:")
    if city == "Stop":
        break
    msc_geodata = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}')

    msc_geodata: list = msc_geodata.json()

    lat: float = msc_geodata[0]['lat']
    lon: float = msc_geodata[0]['lon']

    msc_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}').json()
    print(f"Город {city}:")
    print("температура:", msc_weather["main"]["temp"])
    print("ощущается:", msc_weather["main"]["feels_like"])