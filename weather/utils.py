from typing import Any
import requests


def get_city_coordinates(city: str) -> tuple[float | None, float | None]:
    url = (
        f'https://nominatim.openstreetmap.org/search?q={city}'
        f'&format=json&limit=1'
    )
    response = requests.get(url)
    data = response.json()
    if data:
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        return float(latitude), float(longitude)
    return None, None


def get_weather_info(
        latitude: float | None, longitude: float | None
) -> dict[str, Any]:
    url = (
        f'https://api.open-meteo.com/v1/forecast?'
        f'latitude={latitude}&longitude={longitude}&hourly=temperature_2m'
    )
    response = requests.get(url)
    return response.json()
