import json
import os
import matplotlib.pyplot as plt
import pandas as pd

def load_weather_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Extract relevant data for visualization
    records = []
    for entry in data['list']:
        dt = entry['dt_txt']
        temp = entry['main']['temp']
        humidity = entry['main']['humidity']
        wind = entry['wind']['speed']
        records.append({'datetime': dt, 'temp': temp, 'humidity': humidity, 'wind': wind})
    return pd.DataFrame(records)

def artistic_visualization(df):
    plt.figure(figsize=(12, 6))
    # Artistic: Use color and line width to encode weather
    colors = plt.cm.coolwarm((df['temp'] - df['temp'].min()) / (df['temp'].max() - df['temp'].min()))
    plt.scatter(df['datetime'], df['temp'], c=colors, s=df['humidity'], alpha=0.7, label='Temperature')
    plt.plot(df['datetime'], df['temp'], color='black', linewidth=2, alpha=0.2)
    plt.xticks(rotation=45, ha='right')
    plt.title('Artistic Weather Visualization')
    plt.xlabel('Date/Time')
    plt.ylabel('Temperature (°C)')
    plt.tight_layout()
    # Return the current figure so caller can show or save it
    return plt.gcf()

if __name__ == "__main__":
    DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/weather.json')
    df = load_weather_data(DATA_PATH)
    fig = artistic_visualization(df)
    # Ensure assets directory exists
    ASSETS_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets')
    os.makedirs(ASSETS_DIR, exist_ok=True)
    out_path = os.path.join(ASSETS_DIR, 'visualization.png')
    # Save the figure to assets and also display it
    fig.savefig(out_path, dpi=150)
    print(f"Saved visualization to {out_path}")
    try:
        plt.show()
    except Exception:
        # In headless environments, plt.show() may fail — that's fine
        pass
