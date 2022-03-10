import requests
from Features.speak import speak
import geocoder
g = geocoder.ip('me')

def weather():
    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
        str(g.latlng[0]) + "&lon=" + str(g.latlng[1])
    data = requests.get(api_url)
    data_json = data.json()
    if data_json['cod'] == 200:
        main = data_json['main']
        weather_desc = data_json['weather'][0]
        speak("weather of your current location is : ")
        speak('weather type ' + weather_desc['main'])
        speak('Temperature: ' + str(main['temp']) + 'degree celcius')       
            
# Ladtitude Longititude , current location
def Location():
    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
        str(g.latlng[0]) + "&lon=" + str(g.latlng[1])
    data = requests.get(api_url)
    data_json = data.json()
    if data_json['cod'] == 200:
        speak(str(data_json['coord']['lat']) + 'latitude' + str(data_json['coord']['lon']) + 'longitude')
        speak('Current location is ' + data_json['name'] + data_json['sys']['country'] + 'dia')

## humidity and wind speed
def weather_updates():  
    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
        str(g.latlng[0]) + "&lon=" + str(g.latlng[1])

    data = requests.get(api_url)
    data_json = data.json()
    if data_json['cod'] == 200:
        main = data_json['main']
        wind = data_json['wind']
        speak('Wind speed is ' + str(wind['speed']) + ' metre per second')
        speak('Humidity is ' + str(main['humidity']))
#weather_updates()
#weather()
#Location()
