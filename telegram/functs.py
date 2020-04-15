import requests
import logging
import telegram
import time
from bs4 import BeautifulSoup
from movie import imdbMovie
from vocabulary import Vocab
from weather import weathers
from horoscope import horoscope
######################################33
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import ChatMember
import info
################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class functs:
    def __init__(self,updater,dp):
        self.url=info.url
        self.token=info.token
        self.updater=updater
        self.dp=dp
        self.bot = telegram.Bot(token=self.token)
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
      
    def currency_exchange(self,update,context):
        result=requests.get('https://api.exchangeratesapi.io/latest?base=USD')
        result=result.json()
        response=result['rates']
        key=update.message.text # /currency TRY,USD,10
        cur_list=key.lstrip("/currency ")
        print(cur_list)
        cur_list=cur_list.split(",")
        print(cur_list)
        _result=float(cur_list[2])*(float(response[cur_list[0]])/(float(response[cur_list[1]])))
        time.sleep(2)
        context.bot.send_message(chat_id=update.effective_chat.id,text=f'''
        **************
        {_result}
        **************
        ''')    

    def youtubeSearchSelenium(self,update,context):
            _url="https://www.youtube.com/"
            _msg=update.message.text
            msg_lst=_msg.split(" ")
            msg=msg_lst[1]
            driver=webdriver.Firefox()
            new_url=f"{_url}results?search_query={msg}"
            driver.get(new_url)
            elem=driver.find_element_by_xpath("//*[@id='thumbnail']").get_attribute("href")
            time.sleep(1)
            context.bot.send_message(chat_id=update.effective_chat.id,text=elem)

    def start(self,update,context): 
        chat_user=20200410232728
        _user=telegram.ChatMember(chat_user,"online")
        print(update._effective_user)
        
    def imdbMovies(self,update,context):
        chat_message=update.message.text
        _list=chat_message.split(" ")
        _list.remove("/movie")
        x=imdbMovie("".join(_list)).get_movie()
        context.bot.send_message(chat_id=update.effective_chat.id,text=x)

    def Vocabulary(self,update,context):
        try:
            chat_message=update.message.text
            x=Vocab(chat_message).mean()
            context.bot.send_message(chat_id=update.effective_chat.id,text=x)
        except KeyError:
            context.bot.send_message(chat_id=update.effective_chat.id,text="İnvaild Syntax :(")

    def weather(self,update,context):
        try:
            chat_message=update.message.text
            _lst=chat_message.split(" ")
            _lst.remove("/weather")
            _=weathers("".join(_lst)).get_location()
            context.bot.send_message(chat_id=update.effective_chat.id,text=_)
        except KeyError:
            context.bot.send_message(chat_id=update.effective_chat.id,text="İnvaild Syntax :(")

    def horoscope(self,update,context):
        try:
            chat_message=update.message.text
            _lst=chat_message.split(" ")
            _lst.remove("/horos")
            _=horoscope("".join(_lst)).get_daily()
            context.bot.send_message(chat_id=update.effective_chat.id,text=_)
        except KeyError:
            context.bot.send_message(chat_id=update.effective_chat.id,text="Arıes,Taurus,Gemını,Cancer,Leo,Virgo,Libra,Scorpio,Sagittarius,Capricorn,aquarius,pısces")
    def sendMessag(self,update,context):
        url='https://img-9gag-fun.9cache.com/photo/aKd0E9N_460s.jpg'
        context.bot.send_photo(chat_id=update.effective_chat.id,photo=url)
            
            