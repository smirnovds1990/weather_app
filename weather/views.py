from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .utils import (
    convert_data_to_dataframe, get_city_coordinates, get_weather_info,
    save_city_to_db
)


def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            return redirect(reverse('weather:city', kwargs={'city': city}))
    return render(request, 'weather/index.html')


def get_weather_page(request: HttpRequest, city: str) -> HttpResponse:
    latitude, longitude = get_city_coordinates(city)
    weather_info = get_weather_info(latitude, longitude)
    dataframed_weather_info = convert_data_to_dataframe(weather_info)
    save_city_to_db(city, request.user)
    return render(
        request,
        'weather/city.html',
        context={'weather_info': dataframed_weather_info, 'city': city}
    )


def get_statistics(request: HttpRequest):
    id = request.user.id
    user_cities = ...
    all_cities = ...
    return render(
        request,
        'weather/statistics.html',
        context={
            'user_cities': user_cities,
            'all_cities': all_cities
        }
    )
