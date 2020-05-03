import requests
from bs4 import BeautifulSoup
class imdbMovie():
    def __init__(self,movie):
        self.movie=movie
        self.url=f"https://www.imdb.com/find?q={movie}&ref_=nv_sr_sm"
    
    def get_movie(self):
        html=requests.get(self.url).content
        soup=BeautifulSoup(html,"html.parser")
        items=soup.find("td",{"class":"result_text"}).find('a').get('href')
        _last=f"https://www.imdb.com/{items}?ref_=fn_al_tt_1"
        return _last

    
        

