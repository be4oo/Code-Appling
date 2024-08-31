import requests

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'

city = input('Enter city name: ')

appid = '84bece80722d0f3248e42cf34198d2e5'

res = requests.get(url.format(city, appid))
try:
    data = res.json()
    weather = data['weather'][0]['main']
    temp = data['main']['temp']
    print('Current weather in {} is {} with temperature {} degree.'.format(city, weather, temp))
except:
    print('City not found.')
