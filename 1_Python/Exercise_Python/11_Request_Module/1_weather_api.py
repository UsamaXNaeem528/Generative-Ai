

# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

import requests
import math

api_key = '3ebf8fcd6b2c45f6a170459e81112fa2'
lat = 31.520370
lon = 74.358749
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

main = 0
response = requests.get(url)

if response.status_code == 200:
    data  = response.json()
    temp_kelvin = data['main']['temp']
    temp_celcius = temp_kelvin - 273.15
    print(f'Temp in Lahore {temp_celcius:.2f} * C')
else:
    print("No response")


# print(response.json())
# print(response.status_code)