import requests
import os

from django.http import JsonResponse
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


def get_cords(city: str) -> tuple:
    """Получаем координаты по названию города"""
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}')
    response.raise_for_status()
    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    return lat, lon


def get_weather(lat: float, lon: float) -> dict:
    """Получение данных о погоде по координатам"""
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat='
                            f'{lat}&lon={lon}&appid={API_KEY}&units=metric')
    response.raise_for_status()
    return response.json()


def city_autocomplete(request):
    """API для автодополнения по названиям городов"""
    query = request.GET.get('term', '')

    if not query:
        return JsonResponse([], safe=False)

    # Отправляем запрос к OpenWeather API для поиска городов
    response = requests.get(f'http://api.openweathermap.org/data/2.5/find',
                            params={'q': query, 'appid': API_KEY, 'limit': 5, 'type': 'like'})

    response.raise_for_status()
    cities = response.json().get('list', [])

    # Формируем список городов для автодополнения
    suggestions = [{'label': city['name'], 'value': city['name']} for city in cities]

    return JsonResponse(suggestions, safe=False)
