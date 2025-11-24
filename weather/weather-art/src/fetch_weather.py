import requests
import os

def fetch_weather(api_key, city, output_path):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    with open(output_path, 'w', encoding='utf-8') as f:
        import json
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Weather data saved to {output_path}")

if __name__ == "__main__":
    # Replace with your OpenWeatherMap API key and city
    API_KEY = "2b9538dde358789ed5e953ca730c43fd"  # <-- User's real API key
    CITY = "New York"
    OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../data/weather.json')
    fetch_weather(API_KEY, CITY, OUTPUT_PATH)
