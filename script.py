import requests

from config import API_KEY, BASE_URL


def get_city(city: str, units: str,  api_key: str = API_KEY):
    data = ""
    if units == "F":
        data = "imperial"
    elif units == "C":
        data = "metric"
    params = {
        "q": city,
        "appid": api_key,
        "units": data,
        "lang": "ru"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()


def get_weather(data: dict):
    main = data.get("main", {})
    weather = data.get("weather", [{}])[0]
    return {
        "Город": data.get("name"),
        "Температура": round(main.get("temp")),
        "Ощущается как": round(main.get("feels_like")),
        "Описание": weather.get("description").capitalize()
    }


def get_result(city: str, units: str):
    try:
        data = str()
        response = get_city(city.capitalize(), units)
        weather = get_weather(response)
        for key, value in weather.items():
            data += f"{key}: {value}\n"
        return data
    except Exception as e:
        return "Ошибка", e
