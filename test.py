# GET - получаем данные
# POST - отправляем данные
import requests
import pprint
import json
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
print(API_KEY)
# city = input("Чтобы выбрать город напишите его. Чтобы выйти напишите Stop:")

# while city != "Stop":
#     # Получаем геоданные города Москва. Можешь поставить какой хочешь
#     msc_geodata = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}')

#     # Преобразовываем ответ от API из JSON формата к списку словарей для удобного получения информации с помощью метода json()
#     msc_geodata: list = msc_geodata.json()

#     # Получаем из геоданных ширину и долготу города, чтобы узнать погоду в этой местности
#     lat: float = msc_geodata[0]['lat']
#     lon: float = msc_geodata[0]['lon']

#     # Просмотри эту страницу и попробуй написать код для отправки GET запроса к API и получения данных о погоде
#     # https://openweathermap.org/current#data
#     msc_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}').json()
#     print(f"Город {city}:")
#     print("температура:", msc_weather["main"]["temp"])
#     print("ощущается:", msc_weather["main"]["feels_like"])
#     city = input("Чтобы выбрать город напишите его. Чтобы выйти напишите Stop:")

while True:
    city = input("Чтобы выбрать город напишите его. Чтобы выйти напишите Stop:")
    if city == "Stop":
        break
    # Получаем геоданные города Москва. Можешь поставить какой хочешь
    msc_geodata = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}')

    # Преобразовываем ответ от API из JSON формата к списку словарей для удобного получения информации с помощью метода json()
    msc_geodata: list = msc_geodata.json()

    # Получаем из геоданных ширину и долготу города, чтобы узнать погоду в этой местности
    lat: float = msc_geodata[0]['lat']
    lon: float = msc_geodata[0]['lon']

    # Просмотри эту страницу и попробуй написать код для отправки GET запроса к API и получения данных о погоде
    # https://openweathermap.org/current#data
    msc_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}').json()
    print(f"Город {city}:")
    print("температура:", msc_weather["main"]["temp"])
    print("ощущается:", msc_weather["main"]["feels_like"])