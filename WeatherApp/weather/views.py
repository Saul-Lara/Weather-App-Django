import requests, math
from django.shortcuts import render
from .models import City

def index(request):
    myApiKey = '8b8725efe2207db4e9432a2fdd69b3d7';
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=' + myApiKey
    city = 'Berlin'

    weather_data = []

    cities = City.objects.all()

    for city in cities:
        json_data = requests.get(url.format(city)).json()

        cityWeather = {
            'city' : json_data['name'] + ',' + json_data['sys']['country'],
            'temperature' : str(math.ceil(json_data['main']['temp'] - 273.15)),
            'description' : json_data['weather'][0]['description'],
            'icon' : json_data['weather'][0]['icon'],
        }

        weather_data.append(cityWeather)

    context = {'weather_data' : weather_data}

    return render(request, 'weather/weather.html', context)