import requests
from bs4 import BeautifulSoup

class Vocab():
    def __init__(self,word):
        self.word=word
        _lst=self.word.split(" ")
        _lst.remove("/word")
        _msg="".join(_lst)
        self.url=f"https://www.vocabulary.com/dictionary/{_msg}"

    def mean(self):
        response=requests.get(self.url).content
        soup=BeautifulSoup(response,"html.parser")
        sort=soup.find("p",{"class":"short"})
        return sort.text




        