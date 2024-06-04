import requests

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

def main():
    # Weather API details
    api_key = "d3dda624a81af4587511e0524a1bbc5a"
    lat = 12.5776539
    lon = 106.9349172

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