import requests
import weatherDB
from datetime import datetime, timedelta

def get_weather_forecast(api_key, lat, lon):
    # Construct the API request URL for 5-day forecast
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    # Send a GET request to the API
    response = requests.get(url)
   
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        forecast_data = response.json()
        return forecast_data
    else:
        # Handle errors (e.g., invalid API key, request limits exceeded)
        print(f"Error fetching weather data: {response.status_code}")
        return None

def get_weather_emoji(weather_id):
    # Mapping of weather condition codes to emojis
    emoji_map = {
        # Group 2xx: Thunderstorm
        200: "⛈️", 201: "⛈️", 202: "⛈️", 210: "⛈️", 211: "⛈️", 212: "⛈️", 221: "⛈️", 230: "⛈️", 231: "⛈️", 232: "⛈️",
        # Group 3xx: Drizzle
        300: "🌦️", 301: "🌦️", 302: "🌦️", 310: "🌦️", 311: "🌦️", 312: "🌦️", 313: "🌦️", 314: "🌦️", 321: "🌦️",
        # Group 5xx: Rain
        500: "🌧️", 501: "🌧️", 502: "🌧️", 503: "🌧️", 504: "🌧️", 511: "🌧️", 520: "🌧️", 521: "🌧️", 522: "🌧️", 531: "🌧️",
        # Group 6xx: Snow
        600: "❄️", 601: "❄️", 602: "❄️", 611: "❄️", 612: "❄️", 613: "❄️", 615: "❄️", 616: "❄️", 620: "❄️", 621: "❄️", 622: "❄️",
        # Group 7xx: Atmosphere
        701: "🌫️", 711: "🌫️", 721: "🌫️", 731: "🌫️", 741: "🌫️", 751: "🌫️", 761: "🌫️", 762: "🌫️", 771: "🌫️", 781: "🌪️",
        # Group 800: Clear
        800: "🌞",
        # Group 80x: Clouds
        801: "🌤️", 802: "⛅", 803: "🌥️", 804: "💭"
    }
    # Default emoji if condition is not found
    return emoji_map.get(weather_id, "❓")

def get_weather(api_key, lat, lon):
    # Construct the API request URL
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
   
    # Send a GET request to the API
    response = requests.get(url)
   
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        weather_data = response.json()
        return weather_data
    else:
        # Handle errors (e.g., invalid API key, request limits exceeded)
        print(f"Error fetching weather data: {response.status_code}")
        return None

def main():
    # Weather API details
    api_key = "d3dda624a81af4587511e0524a1bbc5a"
    lat = 12.458851
    lon = 107.175838

    # Get weather forecast data
    forecast_data = get_weather_forecast(api_key, lat, lon)
    #weatherDB.my_Day_Insert("PU", "Saturday", "2024-06-8", "23.95", "20.82", "29.55", "overcast clouds")
    if forecast_data:
        print("Today's Weather Forecast for Pu Ngaol:")
        # Get today's date
        today = datetime.now().date()
       
        # Extract relevant data for each hour
        for forecast in forecast_data['list']:
            forecast_time = datetime.strptime(forecast['dt_txt'], "%Y-%m-%d %H:%M:%S")
            if forecast_time.date() == today and forecast_time.hour <= 23:
                temp = forecast['main']['temp']
                weather_id = forecast['weather'][0]['id']
                weather_description = forecast['weather'][0]['description']
                weather_emoji = get_weather_emoji(weather_id)
               
                # Print the weather information for the hour
                print(f"{forecast_time.strftime('%Y-%m-%d %H:%M:%S')}: {temp}°C, {weather_description} {weather_emoji}")
       
        print("\n5-Day Weather Forecast for Pu Ngaol:")
        # Initialize variables to calculate daily averages
        daily_temps = {}
        daily_weather = {}

        # Calculate average temperature and midday weather for each day
        for forecast in forecast_data['list']:
            forecast_time = datetime.strptime(forecast['dt_txt'], "%Y-%m-%d %H:%M:%S")
            forecast_date = forecast_time.date()
            if forecast_date == today:
                continue  # Skip today's data
            temp = forecast['main']['temp']
            weather_id = forecast['weather'][0]['id']
            weather_description = forecast['weather'][0]['description']
            weather_emoji = get_weather_emoji(weather_id)

            if forecast_date not in daily_temps:
                daily_temps[forecast_date] = []
            daily_temps[forecast_date].append(temp)
           
            # Take midday weather (12:00 PM) for each day
            if forecast_time.hour == 12:
                daily_weather[forecast_date] = (weather_description, weather_emoji)

        # Print the 5-day forecast
        for date, temps in daily_temps.items():
            avg_temp = sum(temps) / len(temps)
            min_temp = min(temps)
            max_temp = max(temps)
            weather_description, weather_emoji = daily_weather.get(date, ("No data", "❓"))
            #weatherDB.my_Day_Insert("PU", "Saturday", "2024-06-8", "23.95", "20.82", "29.55", "overcast clouds")
            weatherDB.my_Day_Insert("PU", "Day", str(date), str(round(avg_temp, 2)), str(round(min_temp,2 )), str(round(max_temp, 2)), str(weather_description))
            #print(f"{date}: Avg Temp: {avg_temp:.2f}°C, Min Temp: {min_temp:.2f}°C, Max Temp: {max_temp:.2f}°C, Midday Weather: {weather_description} {weather_emoji}")
    else:
        print("Unable to retrieve weather forecast data.")
    lat = 12.5776539
    lon = 106.9349172
    
    print("\nSen Monorom")
    # Get weather data
    weather_data = get_weather(api_key, lat, lon)
   
    if weather_data:
        # Extract relevant data
        temp = weather_data['main']['temp']
        weather_id = weather_data['weather'][0]['id']
        weather_description = weather_data['weather'][0]['description']
        weather_emoji = get_weather_emoji(weather_id)
       
        # Print the weather information
        print(f"Temperature: {temp}°C")
        print(f"Weather: {weather_description} {weather_emoji}")
    else:
        print("Unable to retrieve weather data.")

if __name__ == "__main__":
    main()
