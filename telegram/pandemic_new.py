import requests
from bs4 import BeautifulSoup
from pandas.io.html import read_html
import pandas as pd
class hot_corona():
    def __init__(self):
        self.url='https://www.worldometers.info/coronavirus/'

    def get_country_case(self,_country_name): 
        _pandemic=dict()
        response=requests.get('https://www.worldometers.info/coronavirus/').content
        hot_table=read_html(response,attrs={"id":"main_table_countries_today"})
        hot_table[0].drop(["ActiveCases",'Serious,Critical','Serious,Critical','Deaths/1M pop','TotalTests','Tests/ 1M pop'],axis=1,inplace=True)

        country_names=list(hot_table[0]["Country,Other"].head(n=20).iteritems())
        Total_Cases=list(hot_table[0]["TotalCases"].head(n=20).iteritems())
        New_Cases=list(hot_table[0]["NewCases"].head(n=20).iteritems())
        Total_Deaths=list(hot_table[0]["TotalDeaths"].head(n=20).iteritems())
        New_Deaths=list(hot_table[0]["NewDeaths"].head(n=20).iteritems())
        Total_Recovered=list(hot_table[0]["TotalRecovered"].head(n=20).iteritems())

        for i in range(0,20):
            _pandemic[country_names[i][1]]="Total_Cases: {}\n New_Cases: {}\n Total_Deaths: {}\n New_Deaths: {}\n Total_Recovered: {}\n".format(
            Total_Cases[i][1],
            New_Cases[i][1],
            Total_Deaths[i][1],
            New_Deaths[i][1],
            Total_Recovered[i][1]
            )
        return _pandemic[_country_name]

