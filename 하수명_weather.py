from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.weather.go.kr/w/obs-climate/land/city-obs.do?auto_man=m&stn=0&dtm=6&type=t99&reg=100&tm=2022.07.25.11%3A00"

res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

temp= soup.select_one("#weather_table > tbody > tr:nth-child(41) > td:nth-child(6)").string

print("6시간 후 현재 기온 : " , temp)


import requests
import json

apikey ="5fb9004db32a746ad3f4765744dcbc0c"

cities = ["Seoul,KR"]

api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
humidity = []
for name in cities:
    url = api.format(city=name, key=apikey)
    r = requests.get(url)
    data = json.loads(r.text)
    humidity.append(data["main"]["humidity"])

print("현재 습도 : ", humidity)