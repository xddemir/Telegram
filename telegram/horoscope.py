import requests
from bs4 import BeautifulSoup

class horoscope():
    def __init__(self,horo):
        self.horo=horo
        self.url=f'https://www.horoscope.com/star-ratings/today/{horo}'
    def get_daily(self):
        txt=[]
        listo=[]
        letters=[]
        response=requests.get(self.url).content
        soup=BeautifulSoup(response,'html.parser')
        for i in soup.find_all("h3"):
            a=i.find_all("i",{"class":"icon-star-filled highlight"})
            listo.append(a)
        for i in soup.find_all("p"):
            txt.append(i.text)
      
        _list=[["Sex",len(listo[0]),txt[0]],["Hustle",len(listo[1]),txt[1]],["Vibe",len(listo[2]),txt[2]],["Success",len(listo[3]),txt[3]]]
        text=f":{self.horo}: \n "
        for i in _list:
            for j in range(len(i)):
                text+=(f"{i[0]} ")+(f" ⭐️ "*i[1])+"\n"+(f"{i[2]}")+"\n"
                break
        
        return text