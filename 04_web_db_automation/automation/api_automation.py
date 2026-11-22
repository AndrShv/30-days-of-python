import warnings
warnings.filterwarnings("ignore")

import requests


def get_external_weather(city: str) -> dict:
    url = "https://api.open-meteo.com/v1/forecast?latitude=46.48&longitude=30.72&hourly=temperature_2m"

    response = requests.get(url)
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    try:
        data = get_external_weather("Odesa")
        temperatures = data.get("hourly", {}).get("temperature_2m", [])
        current_temp = temperatures[-1] if temperatures else "Н/Д"

        print(f"--- Успешное подключение к API ---")
        print(f"Город: Одесса")
        print(f"Текущая температура на улице: {current_temp}°C")

    except requests.exceptions.HTTPError as e:
        print(f"Ошибка запроса: {e}")