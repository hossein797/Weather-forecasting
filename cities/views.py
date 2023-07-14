from django.shortcuts import render
from .models import Location, Weather
import requests

# Create your views here.

def cities_list(request):
    cities = Location.objects.all()
    context = {"cities": cities}
    return render(request, 'cities/index.html', context)


def forecasts(request, location_id):
    def save_into_db(res):
        temp = Weather()
        location_obj = Location.objects.get(name=city.name)
        temp.location = location_obj

        # Extract the nested values from the dictionary
        values_dict = res['data']['values']

        temp.temperature = values_dict.get('temperature', None)
        temp.temperatureApparent = values_dict.get('temperatureApparent', None)
        temp.humidity = values_dict.get('humidity', None)
        temp.precipitation = values_dict.get('rainIntensity', None)
        temp.wind_speed = values_dict.get('windSpeed', None)
        temp.wind_direction = values_dict.get('windDirection', None)
        temp.conditions = values_dict.get('weatherCode', None)
        temp.weatherDescription = values_dict.get('weatherCode', None)
        temp.icon = values_dict.get('weatherCode', None)
        temp.uvIndex = values_dict.get('uvIndex', None)
        temp.visibility = values_dict.get('visibility', None)
        temp.pressure = values_dict.get('pressureSurfaceLevel', None)
        temp.dewPoint = values_dict.get('dewPoint', None)
        temp.ceiling = values_dict.get('cloudCeiling', None)
        temp.cloudCover = values_dict.get('cloudCover', None)
        temp.windGust = values_dict.get('windGust', None)

        temp.save()

    city = Location.objects.get(id=location_id)
    url = f'https://api.tomorrow.io/v4/weather/realtime?location={city.name}&apikey=WD1MzOW1DrVKyWpESFlVSoIMOemo22Tp'
    headers = {"accept": "application/json"}
    data = requests.get(url, headers=headers)
    response = data.json()  # class dict
    save_into_db(response)
    return render(request, 'cities/forcast.html', {"response": response, "city": city})
