from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .utils import get_city_coordinates, get_weather_info


def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            return redirect(reverse('weather:city', kwargs={'city': city}))
    return render(request, 'weather/index.html')


def get_weather_page(request: HttpRequest, city: str) -> HttpResponse:
    latitude, longitude = get_city_coordinates(city)
    weather_info = get_weather_info(latitude, longitude)
    return render(
        request,
        'weather/city.html',
        context={'weather_info': weather_info, 'city': city}
    )
