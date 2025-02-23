# https://weatherstack.com/
#     """
#     Fetches the latest news headlines from the NewsAPI.
#  Ejemplo de petición
#  https://api.weatherstack.com/current?access_key=5ec835d1bf8459133200cf809b86b908&query=barcelona

from typing import Optional
import requests
import os

os.system("cls")

def get_weather(location: str, celsius: Optional[bool] = False) -> str:
    """
    Get the current weather at the given location using the WeatherStack API.

    Args:
        location: The location (city name).
        celsius: Whether to return the temperature in Celsius (default is False, which returns Fahrenheit).

    Returns:
        A string describing the current weather at the location.
    """
    api_key = "5ec835d1bf8459133200cf809b86b908"  # Replace with your API key from https://weatherstack.com/
    units = "m" if celsius else "f"  # 'm' for Celsius, 'f' for Fahrenheit

    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={location}&units={units}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()

        if data.get("error"):  # Check if there's an error in the response
            return f"Error: {data['error'].get('info', 'Unable to fetch weather data.')}"

        weather = data["current"]["weather_descriptions"][0]
        temp = data["current"]["temperature"]
        temp_unit = "°C" if celsius else "°F"

        return f"The current weather in {location} is {weather} with a temperature of {temp} {temp_unit}."

    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {str(e)}"
    
print("Ejemplo: " + get_weather("Madrid", celsius=True ))  # Ejemplo de uso: obtiene el clima actual en Madrid

# Ahora se lo pedimos por consola al usuario el location y si quiere la temperatura en celsius
ciudad = input("Enter a location: ")
cels = input("Would you like the temperature in Celsius? (y/n): ").lower() == "y"

print(get_weather(ciudad, celsius=cels))