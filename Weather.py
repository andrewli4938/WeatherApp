import requests
import json

class Weather:
    def __init__(self):
        self.lat, self.lon = self.getlocation()
        self.get_weather(self.lat, self.lon)

    def get_weather(self, lat, lon):
        api_endpoint = "https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=8c0d77d15b575685ce72a81e3a7b83ed&units=metric".format(latitude=lat, longitude=lon)
        response = requests.get(api_endpoint)
        data = response.json()
        
        data_arr = json.loads(json.dumps(data))

        weather_description = data_arr["weather"][0]["description"]
        main_temp = data_arr["main"]["temp"]

        print(weather_description, main_temp)

    def getlocation(self):
        city_name = input("Enter city name: ")
        state_code = input("Enter state code: ")
        country_code = input("Enter country code: ")

        api_endpoint = "http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=&appid=8c0d77d15b575685ce72a81e3a7b83ed".format(city_name=city_name, state_code=state_code, country_code=country_code)
        response = requests.get(api_endpoint)
        data = response.json()
        
        data_arr = json.loads(json.dumps(data))

        lat = data_arr[0]['lat']
        lon = data_arr[0]['lon']

        return lat, lon

        

w = Weather() 

