#from twilio.rest import Client
import keys
from datetime import datetime, timedelta
import weatherDB4
import network


#client = Client(keys.account_sid, keys.auth_token)

today = datetime.today().strftime('%Y-%m-%d')
tomorrow = datetime.now().date() + timedelta(1)
fivedays = tomorrow
#todaydate = datetime.
todaytimelimit = int(datetime.today().strftime('%H'))
global starttimecount
print(todaytimelimit)
match todaytimelimit:
        case 21 | 22 | 23 : 
                today = tomorrow
                starttimecount = 0
        case 00 | 1 | 2 : 
                starttimecount = 1
        case 3 | 4 | 5 : 
                starttimecount = 2
        case 6 | 7 | 8 : 
                starttimecount = 3
        case 9 | 10 | 11 : 
                starttimecount = 4
        case 12 | 13 | 14 : 
                starttimecount = 5
        case 15 | 16 | 17 : 
                starttimecount = 6
        case 18 | 19 | 20 : 
                starttimecount = 7
            

hour_repository = ["00:00:00", "03:00:00", "06:00:00",
                   "09:00:00", "12:00:00", "15:00:00",
                   "18:00:00", "21:00:00"]

def get_weather_message_hour(forecast_day_ID):
                temp = weatherDB4.my_W_All_Select_WeatherID("temp", forecast_day_ID)
                weather_id = weatherDB4.my_W_All_Select_WeatherID("weather_id", forecast_day_ID)
                weather_description = weatherDB4.my_W_All_Select_WeatherID("weather_description", forecast_day_ID)
                weather_time = weatherDB4.my_W_All_Select_WeatherID("dt_txt", forecast_day_ID)
                weather_emoji = network.get_weather_emoji(weather_id)
                             
                # Print the weather information for the hour
                #print(f"{weather_time}: {temp}°C, {weather_description} {weather_emoji}")
                weather_return = f"{weather_time}: {temp}°C, {weather_description} {weather_emoji}"

                return weather_return

def get_weather_message_days(weatherID_Day, Day):
#             dt, temp, feels_like, temp_min, temp_max, pressure, sea_level, grnd_level, 
#                 humidity, temp_kf, weather_id, weather_main, weather_description, weather_icon, 
#                 clouds_all, wind_speed, wind_deg, wind_gust, visibility, pop, rain_3h, sys_pod, 
#                 dt_txt, location 
                day = Day
                temp_min = weatherDB4.my_W_All_Select_WeatherID("temp_min", weatherID_Day)
                temp_max = weatherDB4.my_W_All_Select_WeatherID("temp_max", weatherID_Day)
                temp_min = weatherDB4.my_W_All_Select_WeatherID("temp_min", weatherID_Day)
                weather_id = weatherDB4.my_W_All_Select_WeatherID("weather_id", weatherID_Day)
                temp_avg = (temp_min + temp_max)/2
                weather_description = weatherDB4.my_W_All_Select_WeatherID("weather_description", weatherID_Day)
                weather_time = weatherDB4.my_W_All_Select_WeatherID("dt_txt", weatherID_Day).strftime('%Y-%m-%d')
                weather_emoji = network.get_weather_emoji(weather_id)
                             

                #print(f"{weather_time}: Avg Temp: {temp_avg:.2f}°C, Min Temp: {temp_min:.2f}°C, Max Temp: {temp_max:.2f}°C, Midday Weather: {weather_description} {weather_emoji}")
                # Print the weather information for the hour
                
                weather_return = f"{day} {weather_time}: Avg Temp: {temp_avg:.2f}°C, Min Temp: {temp_min:.2f}°C, Max Temp: {temp_max:.2f}°C, Midday Weather: {weather_description} {weather_emoji}"

                return weather_return
# print(todaytimelimit)
# print(todaydate)
# print(tomorrow)
# print(today)
print("Weather of the hour: \n")
for hour in hour_repository[starttimecount:]:
        
        #print(hour)
        weatherID_Hour = weatherDB4.my_Hour_Select_WeatherID("PN", today, hour)
        WanderWeatherHour = get_weather_message_hour(weatherID_Hour)
        print(WanderWeatherHour)
        #print(weatherID_Hour)

#get_weather_message(weatherID_Day)

print("\n Weather of the next 5 day: \n")
for days in range(4): 
        weatherID_Day = weatherDB4.my_Day_Select_WeatherID("PN", fivedays)
        weatherDay_Day = weatherDB4.my_Day_Select_Day("PN", fivedays)
        #get_weather_message_days(weatherID_Day)
        WanderWeatherDay = get_weather_message_days(weatherID_Day, weatherDay_Day)
        fivedays = fivedays + timedelta(1)
        print(WanderWeatherDay)
# message = client.messages.create (
#     body = "hey its ash, it works :)",
#     from_=keys.twilio_number,
#     to=keys.my_phone_number

# )

# print(message.body)