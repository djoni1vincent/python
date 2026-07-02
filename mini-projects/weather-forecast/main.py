
import requests

headers = {
    "User-Agent": "MyPythonApp/1.0 djoni8vincent@gmail.com"
}

def get_weather(lat, lon):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return response.json()
if __name__ == "__main__":
    data = get_weather(68.87, 17.85) # sjovegan


details = data["properties"]["timeseries"][0]["data"]["instant"]["details"]
ts = data["properties"]["timeseries"][0]["data"]

temp = details["air_temperature"]
wind = details["wind_speed"]

print(f"Температура: {temp} celsium")
print(f"Ветер: {wind} m/s")

if(temp > 5):
    print("Ну так-то нормульок \nИ")
elif(temp <= 0):
    print("Дальше Бога нет. \nИ")
elif(temp <= 5):
    print("WINTER IS COMMING \nИ")

if(wind <= 2.5):
    print("Ветерок слабенький, жить можна")
elif(wind >= 2.5 and wind <= 4):
    print("Неприятный ветерок, надобы шарфик")
else:
    print("сочуствую, ветерок тебе НАХУЙ снесет.")


    