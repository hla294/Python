import requests
import twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall "
api_key = "70ad3656455080593dd1fd0a7eafbfec"

weather_params = {
    "lat": 49.282730,
    "lon": -123.120735,
    "appid": api_key,
    "exclude": "current, minutely, daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.message \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from="+123456789",
        to = "Your verified number"
    )
    print(message.status)




    #print("Bring an umbrella.")


# print(weather_data["hourly"][0]["weather"][0]["id"])

