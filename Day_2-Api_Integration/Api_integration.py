import json
import pandas as pd
import requests

api_key = "d17979af7398e2ec00b25da98f30ae15"  # Replace with your actual API key
city = "London"  # You can change this to any city you want
base_url = "http://api.openweathermap.org/data/2.5/weather"


params = {
    'q': city,
    'appid': api_key,
    'units': 'metric'  # This will return the temperature in Celsius
}


response = requests.get(base_url, params=params)


if response.status_code == 200:
    data = response.json()
    
    weather_data = {
        'City': [data['name']],
        'Temperature (C)': [data['main']['temp']],
        'Weather': [data['weather'][0]['description']],
        'Humidity (%)': [data['main']['humidity']],
        'Pressure (hPa)': [data['main']['pressure']]
    }
    
    df=pd.DataFrame(weather_data)
    df.to_csv('weather_data.csv', index= False)
else:
    print(f"Error: {response.status_code}")

