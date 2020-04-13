import requests
import json
class theMoviedb:
    def __init__(self):
        self.url="https://api.themoviedb.org/3"
        self.api_key="5efeb66d05f6da394f2a912290f5f25f"

    def searchMovie(self,name):
        response=requests.get(self.url+'/search/movie?api_key='+self.api_key+f'&language=en-US&query={name}&page=1&include_adult=false')
        json_dic=response.json()
        for original_name in json_dic['results']:
            print(original_name['title'])
    
    def searchPeopleMovie(self,name):
        response=requests.get(f"{self.url}/search/person?api_key={self.api_key}&language=en-US&query={name}&page=1&include_adult=false")
        json_dic=response.json()
        new_lst=[]
        for j in json_dic['results']:
            new_lst.append(j['known_for'])
        for i in new_lst[0]:
            print(i['title'])
    
    def popularMovie(self):
        response=requests.get(f"{self.url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        json_dic=response.json()
        for item in json_dic["results"]:
            print(f"Name: {item['original_title']}   Rate:  {item['vote_average']}   ")
            print("*************************************************************************")

    


        





_moviedb=theMoviedb()
_moviedb.popularMovie()
#_moviedb.searchPeopleMovie("jason statham")
# _moviedb.searchMovie("walking")

