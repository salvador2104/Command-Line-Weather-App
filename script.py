import requests
import json
def k_to_f(kelvin):
  celcius = kelvin - 273
  fahrenheit = (9/5 * celcius) + 32
  return int(fahrenheit)
def get_weather_data(city, api_key):
    geocode_r = requests.get('http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API}'.format(city=city,API = api_key))
    geocode_json = json.loads(geocode_r.text)
    geocode = geocode_json[0]
    lon = geocode['lon']
    lat = geocode['lat']
    weather_data_r = requests.get('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}'.format(lat=lat, lon=lon, API=api_key))
    weather_data_json = json.loads(weather_data_r.text)
    return weather_data_json
    

def display_weather_data(data):
  weather = data['weather']
  description = weather[0]['description']
  city = data['name']
  main = data['main']
  temp = k_to_f(main['temp'])
  humidity= main['humidity']
  tempmax = k_to_f(main['temp_max'])
  tempmin = k_to_f(main['temp_min'])
  suffix = ''
  if description[-1] != 's':
    suffix = 'a '
  print('The weather today in {city} is {temp}\N{DEGREE SIGN} with {suffix}{weather}.'.format(city=city, weather=description,temp=temp,suffix=suffix))
  print('Today\'s maximum temperature will be {}\N{DEGREE SIGN}F'.format(tempmax))
  print('Today\'s minumum temperature will be {}\N{DEGREE SIGN}F'.format(tempmin))
def main():
    api_key = "7abf499891232cb42d67dea20fea0c1f"
    city = input("Enter the city name: ")

    data = get_weather_data(city, api_key)
    display_weather_data(data)

main()
