#from twilio.rest import Client
import keys
from datetime import datetime
import weatherDB4
import network


#client = Client(keys.account_sid, keys.auth_token)

today = datetime.today().strftime('%Y-%m-%d')
#todaydate = datetime.now().date()
todaytimelimit = datetime.today().strftime('%H')
match todaytimelimit:
        case 00 | 01: 
                print("yo")

hour_repository = ["00:00:00", "03:00:00", "06:00:00",
                   "09:00:00", "12:00:00", "15:00:00",
                   "18:00:00", "21:00:00"]
def get_weather_message(forecast_day_ID):
                temp = weatherDB4.my_W_All_Select_WeatherID("temp", forecast_day_ID)
                weather_id = weatherDB4.my_W_All_Select_WeatherID("weather_id", forecast_day_ID)
                weather_description = weatherDB4.my_W_All_Select_WeatherID("weather_description", forecast_day_ID)
                weather_time = weatherDB4.my_W_All_Select_WeatherID("dt_txt", forecast_day_ID)
                weather_emoji = network.get_weather_emoji(weather_id)
                             
                # Print the weather information for the hour
                #print(f"{weather_time}: {temp}°C, {weather_description} {weather_emoji}")
                weather_return = f"{weather_time}: {temp}°C, {weather_description} {weather_emoji}"

                return weather_return

weatherID_Day = weatherDB4.my_Day_Select_WeatherID("PN", today)
print(todaytimelimit)
#print(todaydate)
print(today)
# for hour in hour_repository:
        
#         print(hour)
        #weatherID_Hour = weatherDB4.my_Hour_Select_WeatherID("PN", today2, hour)
        #WanderWeatherHour = get_weather_message(weatherID_Hour)
        #print(WanderWeatherHour)
#print(weatherID_Day)
#get_weather_message(weatherID_Day)
#WanderWeatherDay = get_weather_message(weatherID_Day)
#print(WanderWeatherDay)
# message = client.messages.create (
#     body = "hey its ash, it works :)",
#     from_=keys.twilio_number,
#     to=keys.my_phone_number

# )

# print(message.body)