"""
Weather reporter module — fetches weather data from external APIs.

This module calls real HTTP APIs. Your tests should NOT make real HTTP calls.
Use unittest.mock.patch to replace requests.get with mocks.

NOTE: Do NOT modify this file. Write tests that work with this code as-is.
"""

import requests


API_KEY = "your-api-key"  # In production, this would be an environment variable


def get_current_weather(city: str) -> dict:
    """
    Fetch current weather for a city from OpenWeatherMap.

    Args:
        city: City name (e.g., "San Francisco").

    Returns:
        dict with keys: city, temp_c, description, humidity, wind_speed.
        Returns None if the API call fails.

    Raises:
        ValueError: If city is empty.
    """
    if not city or not city.strip():
        raise ValueError("City cannot be empty")

    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "city": data["name"],
        "temp_c": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
    }


def get_weather_summary(cities: list) -> dict:
    """
    Fetch weather for multiple cities and return a summary.

    Args:
        cities: List of city names.

    Returns:
        dict mapping city name to weather dict (or None if failed).
        Example: {"San Francisco": {...}, "New York": None}
    """
    summary = {}
    for city in cities:
        try:
            summary[city] = get_current_weather(city)
        except (ValueError, requests.exceptions.RequestException):
            summary[city] = None
    return summary


def format_weather_report(city: str, weather: dict) -> str:
    """
    Format weather data as a human-readable report.

    Args:
        city: City name.
        weather: dict from get_current_weather().

    Returns:
        Formatted string like:
        "Weather in San Francisco: 18°C, clear sky, Humidity: 65%, Wind: 3.5 m/s"

    Raises:
        ValueError: If weather dict is None or missing required keys.
    """
    if weather is None:
        return f"Weather in {city}: unavailable"

    required_keys = ["temp_c", "description", "humidity", "wind_speed"]
    for key in required_keys:
        if key not in weather:
            raise ValueError(f"Missing required key: {key}")

    return (
        f"Weather in {city}: {weather['temp_c']}°C, "
        f"{weather['description']}, "
        f"Humidity: {weather['humidity']}%, "
        f"Wind: {weather['wind_speed']} m/s"
    )
