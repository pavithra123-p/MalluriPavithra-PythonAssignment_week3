# Exercise 4
# Weather Data Fetcher & Analyzer

# Import requests library to make HTTP API calls
import requests
import csv
from datetime import datetime

# --------------------------------
# Function 1: Fetch weather data
# --------------------------------
def fetch_weather(city: str, api_key: str) -> dict:
    try:
        # OpenWeatherMap API endpoint URL
        url = "https://api.openweathermap.org/data/2.5/weather"

        # Parameters to be sent with API request
        params = {
            "q": city,           # City name entered by user
            "appid": api_key,    # API key for authentication
            "units": "metric"    # Temperature in Celsius
        }

        # Send GET request to the API with a timeout of 10 seconds
        response = requests.get(url, params=params, timeout=10)

        # Check for unsuccessful HTTP response
        if response.status_code != 200:
            return {
                "error": response.json().get("message", "Unknown error")
            }

        # Return JSON response if request is successful
        return response.json()

    # Handle request timeout error
    except requests.exceptions.Timeout:
        return {"error": "Request timed out. Please try again."}

    # Handle network connection error
    except requests.exceptions.ConnectionError:
        return {"error": "Network connection error."}

    # Handle any unexpected error
    except Exception as e:
        return {"error": str(e)}


# --------------------------------
# Function 2: Analyze weather data
# --------------------------------
def analyze_weather(weather_data: dict) -> str:
    # If error exists in response, return it
    if "error" in weather_data:
        return weather_data["error"]

    try:
        # Extract temperature, humidity, and wind speed
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        # Determine temperature category
        if temp <= 10:
            summary = "Cold (≤10°C)"
        elif 11 <= temp <= 24:
            summary = "Mild (11–24°C)"
        else:
            summary = "Hot (≥25°C)"

        # List to store warning messages
        alerts = []

        # Check for high wind condition
        if wind_speed > 10:
            alerts.append("High wind alert!")

        # Check for high humidity condition
        if humidity > 80:
            alerts.append("Humid conditions!")

        # Append alerts to summary if any exist
        if alerts:
            summary += " | " + " ".join(alerts)

        # Return final weather summary
        return summary

    # Handle missing data in API response
    except KeyError:
        return "Incomplete weather data received."


# --------------------------------
# Function 3: Log weather data to file
# --------------------------------
def log_weather(city: str, filename: str):
    # Fetch weather data for the given city
    weather_data = fetch_weather(city, api_key)

    # If error occurs, display it and exit function
    if "error" in weather_data:
        print("Error:", weather_data["error"])
        return

    # Extract required values from API response
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    # Get current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open CSV file in append mode
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        # Write weather data as a new row
        writer.writerow([timestamp, city, temp, humidity, wind_speed])


# Store API key obtained from OpenWeatherMap
api_key = "85a83f6483452fdd3655c83053d68ae6"

# Take city name input from user
city = input("Enter city name: ").strip()

# Fetch weather data
weather_data = fetch_weather(city, api_key)

# Analyze fetched weather data
result = analyze_weather(weather_data)

# Display weather analysis result
print("\nWeather Analysis:")
print(result)

# Log weather data into CSV file
log_weather(city, "weather_log.csv")

# Confirm data logging
print("Weather data saved to weather_log.csv")
