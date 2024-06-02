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
        weather_description = weather_data['weather'][0]['description']
       
        # Print the weather information
        print(f"Temperature: {temp}°C")
        print(f"Weather: {weather_description}")

if __name__ == "__main__":
    main()

