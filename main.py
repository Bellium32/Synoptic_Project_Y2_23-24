from twilio.rest import Client
import keys
from datetime import datetime
import weatherDB4

client = Client(keys.account_sid, keys.auth_token)

today = datetime.today().strftime('%Y-%m-%d')

weatherID = weatherDB4.my_Day_Select_WeatherID("PN", today)
message = client.messages.create (
    body = "hey its ash, it works :)",
    from_=keys.twilio_number,
    to=keys.my_phone_number

)

print(message.body)