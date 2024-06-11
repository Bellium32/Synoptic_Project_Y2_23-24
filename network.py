import requests
import weatherDB4
from datetime import datetime, timedelta, date
import calendar

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

def hellhellhell(forecast, forecast_time):
    #print(forecast)
    
        # Extract data from JSON
    main = forecast['main']
    #print(main['temp'])
    weather = forecast['weather'][0]
    wind = forecast['wind']
    clouds_all = forecast['clouds']['all']
    visibility = forecast['visibility']
    pop = forecast['pop']
    #rain_3h = forecast['rain']['3h'] 
    sys_pod = forecast['sys']['pod']
    dt = forecast['dt']
    dt_txt = forecast['dt_txt']
    
    wInfo_row_exist = weatherDB4.my_WeatherInfo_Select_Check("PN", dt_txt)
    # Insert into weatherTemp table and get the ID
    if wInfo_row_exist == False:
        #Checks to see if a row that has the date and location already exists
        weatherDB4.my_WeatherInfo_Insert(
        dt, main['temp'], main['feels_like'], main['temp_min'], main['temp_max'],
        main['pressure'], main['sea_level'], main['grnd_level'], main['humidity'], main['temp_kf'],
        weather['id'], weather['main'], weather['description'], weather['icon'],
        clouds_all, wind['speed'], wind['deg'], wind['gust'],
        visibility, pop, 0.12, sys_pod, dt_txt, "PN")
        
    elif wInfo_row_exist == True:
        #If it does the existing row is updated with the new data
        weatherDB4.my_WeatherInfo_Update(
        dt, main['temp'], main['feels_like'], main['temp_min'], main['temp_max'],
        main['pressure'], main['sea_level'], main['grnd_level'], main['humidity'], main['temp_kf'],
        weather['id'], weather['main'], weather['description'], weather['icon'],
        clouds_all, wind['speed'], wind['deg'], wind['gust'],
        visibility, pop, 0.12, sys_pod, dt_txt, "PN")

   
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
    
    #Change here
    
    #weatherDB.my_Day_Insert("PU", "Saturday", "2024-06-8", "23.95", "20.82", "29.55", "overcast clouds")
    if forecast_data:
        print("Today's Weather Forecast for Pu Ngaol:")
        # Get today's date
        today = datetime.now().date()
        
        # Extract relevant data for each hour
        for forecast in forecast_data['list']:
            
            forecast_time = datetime.strptime(forecast['dt_txt'], "%Y-%m-%d %H:%M:%S")
            forecast_date = forecast_time.date()
            forecast_day_time = forecast_time.time()
            forecast_ID = hellhellhell(forecast, forecast_time)
            
            if forecast_time.date() == today and forecast_time.hour <= 23:
                forecast_day_ID = weatherDB4.my_Hour_Select_WeatherID("PN", forecast_date, forecast_day_time)
                
                
                temp = weatherDB4.my_W_All_Select_WeatherID("temp", forecast_day_ID)
                weather_id = weatherDB4.my_W_All_Select_WeatherID("weather_id", forecast_day_ID)
                weather_description = weatherDB4.my_W_All_Select_WeatherID("weather_description", forecast_day_ID)
                weather_emoji = get_weather_emoji(weather_id)
                #temp = forecast['main']['temp']
                # weather_id = forecast['weather'][0]['id']
                # weather_description = forecast['weather'][0]['description']
                # weather_emoji = get_weather_emoji(weather_id)
               
               
                # Print the weather information for the hour
                print(f"{forecast_time.strftime('%Y-%m-%d %H:%M:%S')}: {temp}°C, {weather_description} {weather_emoji}")
       
        print("\n5-Day Weather Forecast for Pu Ngaol:")
        # Initialize variables to calculate daily averages
        daily_temps = {}
        daily_weather = {}

        # Calculate average temperature and midday weather for each day
        for forecast in forecast_data['list']:
            
            forecast_time = datetime.strptime(forecast['dt_txt'], "%Y-%m-%d %H:%M:%S")
            
            #So if here we're stripping forcast's time from the forcast_data, is there a place where 
            #we're stripping the forcasts details that we care about as well?
            forecast_date = forecast_time.date()
            forecast_day_day = calendar.day_name[forecast_time.weekday()]
            forecast_day_time = forecast_time.time()
            
            hour_row_exist = weatherDB4.my_Hour_Select_Check("PN", str(forecast_date), str(forecast_day_time))
            day_row_exist = weatherDB4.my_Day_Select_Check("PN", str(forecast_date))
            WEATHERWIZARD = weatherDB4.my_W_Info_Select_WeatherID("PN", forecast_time)
            forecast_ID = int(WEATHERWIZARD[0])
            
            if str(forecast_day_time) == "12:00:00":
                if day_row_exist == False:
                    
                    weatherDB4.my_Day_Insert("PN", str(forecast_day_day), str(forecast_date), forecast_ID)           
                elif day_row_exist == True:
                    weatherDB4.my_Day_Update_Weather(forecast_ID, "PN", str(forecast_date))
                    
            if hour_row_exist == False:
                 weatherDB4.my_Hour_Insert("PN", str(forecast_day_time), str(forecast_date), forecast_ID)
            
            elif hour_row_exist == True:
                 weatherDB4.my_Hour_Update_Weather(forecast_ID, "PN", str(forecast_date), str(forecast_day_time))
            if forecast_date == today:
                
                continue  # Skip today's data
            
            forecast_day_ID = weatherDB4.my_Hour_Select_WeatherID("PN", forecast_date, forecast_day_time)
                
                
            temp = weatherDB4.my_W_All_Select_WeatherID("temp", forecast_day_ID)
            weather_id = weatherDB4.my_W_All_Select_WeatherID("weather_id", forecast_day_ID)
            weather_description = weatherDB4.my_W_All_Select_WeatherID("weather_description", forecast_day_ID)
            weather_emoji = get_weather_emoji(weather_id)
            
            # temp = forecast['main']['temp']
            # weather_id = forecast['weather'][0]['id']
            # weather_description = forecast['weather'][0]['description']
            # weather_emoji = get_weather_emoji(weather_id)
            

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
            
            print(f"{date}: Avg Temp: {avg_temp:.2f}°C, Min Temp: {min_temp:.2f}°C, Max Temp: {max_temp:.2f}°C, Midday Weather: {weather_description} {weather_emoji}")
       
            #
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
