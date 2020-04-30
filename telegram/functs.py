import requests
import logging
import telegram
import time
import os
from bs4 import BeautifulSoup
from movie import imdbMovie
from vocabulary import Vocab
from weather import weathers
from horoscope import horoscope
from reddit_meme import reddit
from pandemic_new import hot_corona
######################################33
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import ChatMember
from telegram import Message
from telegram import Chat
from telegram import User
import info
################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class functs:
    def __init__(self,updater,dp):
        self.forbidden_words={"sex","darina","haksim"}
        self.counter=0
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
        _=reddit(info.password,info.username).get_meme()
        context.bot.send_photo(chat_id=update.effective_chat.id,photo=_)

    def sendGif(self,update,context):
        _=reddit(info.password,info.username).get_gif()
        context.bot.send_video(chat_id=update.effective_chat.id,video=_)

    def sendPandemic(self,update,context):
        chat_message=update.message.text
        _lst=chat_message.split(" ")
        if len(_lst)<1:
            _=hot_corona().get_country_case("World")
        else:       
            _lst.remove("/pandemic")
            _=hot_corona().get_country_case("".join(_lst))
        context.bot.send_message(chat_id=update.effective_chat.id,text=_)
    
    def kick_member(self,update,context):
        message=update.message
        reply=message.reply_to_message
        reply_id=reply.from_user.id
        reply_name=reply.from_user.name
        try:
            context.bot.send_message(chat_id=update.effective_chat.id,text=reply_name+","+"KICK!")
            context.bot.send_photo(chat_id=update.effective_chat.id,photo=info.coffin1)
            self.bot.kick_chat_member(update.effective_chat.id,reply_id)
        except:
            context.bot.send_message(chat_id=update.effective_chat.id,text=reply_name+","+"KICK!")
            context.bot.send_photo(chat_id=update.effective_chat.id,photo=info.coffin1)
    
    def welcome_member(self,update,context):
        message=update.message
        user=message.new_chat_members[0]
        user_name=user.username
        name=message.new_chat_members[0].name
        try:
            context.bot.send_message(chat_id=update.effective_chat.id,text=info.welcome.format(user_name))
        except:
            context.bot.send_message(chat_id=update.effective_chat.id,text=info.welcome.format(name))

    def remove_forbidden_words(self,update,context):
        _msg=update.message
        txt=_msg.text
        for i in self.forbidden_words:
            if i in txt:
                self.bot.delete_message(update._effective_chat.id,update._effective_message.message_id)
                context.bot.send_message(chat_id=update.effective_chat.id,text="Don't be rude")
    
    def help_bot(self,update,context):
        print("help")
        context.bot.send_message(chat_id=update.effective_chat.id,text=info._help)

    def graph_pandemic(self,update,context):
        print("start")
        chat_message=update.message
        txt=chat_message.txt
        a=txt.split(" ")
        a.remove("/pgraph")
        hot_corona().plot("".join(a))
        #local=os.path.dirname(os.path.abspath("corona.png"))
        context.bot.send_document(update.effective_chat.id,document=open('corona.jpg','rb'))
        print("Completed")

        

















            