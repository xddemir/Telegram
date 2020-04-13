from bs4 import BeautifulSoup
import requests

_url="https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv"

html=requests.get(_url).content
soup=BeautifulSoup(html,"html.parser")
print(soup)
items=soup.find('table',{'class':'chart full-width'}).find({'tbody':'lister-list'})
#for item in items:
#    print(item.find_all("tr").find("td",{'class':'titleColumn'}).find("a").text)


