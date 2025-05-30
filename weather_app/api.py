import requests


def get_weather(city: str):
    """
    Получает прогноз погоды для города через Open-Meteo API.
    """
    url = (f"https://api.open-meteo.com/v1/forecast?current_weather=true&hourly=temperature_2m,precipitation_sum,"
           f"weathercode&timezone=Europe%2FMoscow")
    params = {
        "q": city,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
