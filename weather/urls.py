from django.urls import path

from . import views


app_name = 'weather'

urlpatterns = [
    path('', views.index, name='index'),
    path('<city>/', views.get_weather_page, name='city')
]
