import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

payload = {
    "q": city,
    "appid": API_KEY,
    "units": "metric" 
}

response = requests.get(BASE_URL, params=payload)

if response.status_code == 200:
    weather_data = response.json()

    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']
    city_name = weather_data['name']
    country = weather_data['sys']['country']
    
    print(f"\n🌤️ Weather in {city_name}, {country}")
    print(f"🌡️ Temperature: {temp}°C (feels like {feels_like}°C)")
    print(f"💧 Humidity: {humidity}%")
    print(f"📝 Description: {description.capitalize()}")
    
elif response.status_code == 404:
    print("❌ City not found.")
elif response.status_code == 401:
    print("❌ Invalid API Key. (Did you just generate it? It might take 10 mins to activate!)")
else:
    print(f"❌ Error: {response.status_code}")