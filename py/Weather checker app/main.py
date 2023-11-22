import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "69f04e4613056b159c2761a9d9e664d2"

weather_params = {
    "lat" : 51.759050,
    "lon" : 19.458600,
    "appid" : api_key,
    "exclude" : "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params =  weather_params)
response.raise_for_status()
weather_data = response.json()

new = weather_data["hourly"]
ID = [i["weather"][0]["id"] for i in new]

will_rain = False

for i in ID[:12]:
    if i < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella.")