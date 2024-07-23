from datetime import timedelta
from typing import Any

import requests
import requests_cache

from .constants import (
    COORDINATES_FORMAT, COORDINATES_LIMIT, COORDINATES_URL, WEATHER_DETAILS,
    WEATHER_URL
)

requests_cache.install_cache(
    'city_coordinates_cache', expire_after=timedelta(hours=24)
)


def get_city_coordinates(city: str) -> tuple[float | None, float | None]:
    params = {
        'q': city,
        'format': COORDINATES_FORMAT,
        'limit': COORDINATES_LIMIT
    }
    response = requests.get(COORDINATES_URL, params=params)

    # DELETE IT!!!
    if response.from_cache:
        print(f"Using cached response for {city}")
    else:
        print(f"Fetching new response for {city}")
    # DELETE IT!!!

    data = response.json()
    if data:
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        return float(latitude), float(longitude)
    return None, None


def get_weather_info(
        latitude: float | None, longitude: float | None
) -> dict[str, Any]:
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'hourly': WEATHER_DETAILS
    }
    response = requests.get(WEATHER_URL, params=params)
    return response.json()
