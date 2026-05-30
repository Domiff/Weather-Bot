import aiohttp

from core.config import config


class WeatherClient:
    def __init__(self, api_key: str, base_url: str):
        self._api_key = api_key
        self._base_url = base_url

    async def fetch(self, city: str, units: str) -> dict:
        unit_param = "metric" if units == "C" else "imperial"
        params = {
            "q": city,
            "appid": self._api_key,
            "units": unit_param,
            "lang": "ru",
        }
        async with (
            aiohttp.ClientSession() as session,
            session.get(self._base_url, params=params) as resp,
        ):
            resp.raise_for_status()
            return await resp.json()

    @staticmethod
    def format(data: dict) -> str:
        main = data.get("main", {})
        weather = data.get("weather", [{}])[0]
        return (
            f"Город: {data.get('name')}\n"
            f"Температура: {round(main.get('temp'))}°\n"
            f"Ощущается как: {round(main.get('feels_like'))}°\n"
            f"Описание: {weather.get('description', '').capitalize()}"
        )


weather_client = WeatherClient(
    api_key=config["api_key"],
    base_url=config["base_url"],
)
