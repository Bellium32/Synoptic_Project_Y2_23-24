#from twilio.rest import Client
import keys
from datetime import datetime
import weatherDB4
import network


#client = Client(keys.account_sid, keys.auth_token)

today = datetime.today().strftime('%Y-%m-%d')

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
print(weatherID_Day)
#get_weather_message(weatherID_Day)
Wanderweather = get_weather_message(weatherID_Day)
print(Wanderweather)
# message = client.messages.create (
#     body = "hey its ash, it works :)",
#     from_=keys.twilio_number,
#     to=keys.my_phone_number

# )

# print(message.body)