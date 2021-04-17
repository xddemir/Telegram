import requests
from bs4 import BeautifulSoup

class weathers():
    def __init__(self,message):
        self.message=message
        self.api_key="api_key"
        self._url=f'http://api.openweathermap.org/data/2.5/weather?q={self.message}&appid={self.api_key}'

    def get_location(self):
        req=requests.get(self._url)
        _json=req.json()
        description=_json['weather'][0]['description']
        tempature=_json['main']['temp']
        tempature=tempature-273
        tempature=round(tempature,2)
        return f"{self.message} : {tempature}°C , ☁️ {description}"
