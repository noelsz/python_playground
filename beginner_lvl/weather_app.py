import requests
import json


def weather(api_key, location):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def weather_display(weather_data):
    if weather_data:
        print(f"Current weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Weather: {weather_data['weather'][0]['main']}")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {round((weather_data['main']['temp'] - 273.15), 2)}C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind speed: {weather_data['wind']['speed']}m/s")
    else:
        print("An error occurred while trying to retrieve weather data.")


api_key = input("Your OpenWeatherMap API key: ")
location = input("Enter the location (city, country): ")

weather_display(weather(api_key, location))
