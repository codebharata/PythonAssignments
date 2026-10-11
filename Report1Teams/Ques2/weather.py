
import requests
import json
from datetime import datetime


def fetch_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m,weather_code",
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        current = data["current"]

        temperature = current["temperature_2m"]
        wind_speed = current["wind_speed_10m"]
        weather_code = current["weather_code"]
        timezone = data["timezone"]
        time = current["time"]

        weather_conditions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snowfall",
            73: "Moderate snowfall",
            75: "Heavy snowfall",
            80: "Rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            95: "Thunderstorm"
        }

        condition = weather_conditions.get(
            weather_code, "Unknown weather condition"
        )

        report = (
            "WEATHER REPORT\n"
            "-------------------------\n"
            f"Latitude: {latitude}\n"
            f"Longitude: {longitude}\n"
            f"Date and Time: {time}\n"
            f"Timezone: {timezone}\n"
            f"Temperature: {temperature} °C\n"
            f"Wind Speed: {wind_speed} km/h\n"
            f"Weather Condition: {condition}\n"
        )

        print(report)

        with open("weather_report.txt", "w", encoding="utf-8") as file:
            file.write(report)

        print("Report saved to weather_report.txt")

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")

    except requests.exceptions.HTTPError as error:
        print("HTTP error:", error)

    except requests.exceptions.RequestException as error:
        print("Network error:", error)

    except (KeyError, ValueError, TypeError) as error:
        print("Error processing weather data:", error)


if __name__ == "__main__":
    latitude = 19.0760
    longitude = 72.8777

    fetch_weather(latitude, longitude)