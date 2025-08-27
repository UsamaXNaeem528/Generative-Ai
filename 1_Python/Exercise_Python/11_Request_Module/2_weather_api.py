import requests

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
api_key = '3ebf8fcd6b2c45f6a170459e81112fa2'

# Prompt the user to enter the city name
city_name = input("Enter a city name: ")

# Construct the URL to get weather data for the specified city in Celsius
# The 'q' parameter is for the city name, and 'units=metric' specifies Celsius
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    # print(response.json())
    data = response.json()
    
    # Access the city name and temperature from the JSON response
    city = data['name']
    temp_celsius = data['main']['temp']
    
    print(f"The temperature in {city} is: {temp_celsius}°C")
    print(f"Description {data['name']}\n{data['weather'][0]['description']}")
else:
    # Print an error message if the city is not found or if there's another issue
    print(f"Error: Could not retrieve data. Status code: {response.status_code}")
    print(f"Response: {response.json().get('message', 'No message available')}")
    
    
