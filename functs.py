import requests
import logging
import telegram
import time
import info
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
################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class functs:
    def __init__(self,updater,dp):
        self.forbidden_words={"sex","haksim"}
        self.counter=0
        self.url=info.url
        self.token=info.token
        self.updater=updater
        self.dp=dp
        self.bot = telegram.Bot(token=self.token)
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
      
    def currency(self,update,context):
        result=requests.get('https://api.exchangeratesapi.io/latest?base=USD')
        result=result.json()
        response=result['rates']
        key=update.message.text # /currency TRY,USD,10
        cur_list=key.lstrip("/currency ")
        cur_list=cur_list.split(" ")
        _result=float(cur_list[2])*(float(response[cur_list[0]])/(float(response[cur_list[1]])))
        time.sleep(2)
        _result=round(_result,2)
        context.bot.send_message(chat_id=update.effective_chat.id,text=str(_result)+" "+cur_list[0]+" 💰")

    def youtube(self,update,context):
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

    def movie(self,update,context):
        chat_message=update.message.text
        _list=chat_message.split("")
        _list.remove("/movie")
        listo=[i.lower().capitalize() for i in _list]
        x=imdbMovie("".join(listo)).get_movie()
        context.bot.send_message(chat_id=update.effective_chat.id,text=x)

    def word(self,update,context):
        try:
            chat_message=update.message.text
            chat_message.lower().capitalize()
            x=Vocab(chat_message).mean()
            context.bot.send_message(chat_id=update.effective_chat.id,text=x)
        except KeyError:
            context.bot.send_message(chat_id=update.effective_chat.id,text="İnvaild Syntax :(")

    def weather(self,update,context):
        try:
            chat_message=update.message.text
            _lst=chat_message.split("")
            _lst.remove("/weather")
            listo=[i.lower().capitalize() for i in _lst]
            _=weathers(" ".join(listo)).get_location()
            context.bot.send_message(chat_id=update.effective_chat.id,text=_)
        except KeyError:
            context.bot.send_message(chat_id=update.effective_chat.id,text="İnvaild Syntax :(")

    def horos(self,update,context):
        try:
            chat_message=update.message.text
            _lst=chat_message.split(" ")
            _lst.remove("/horos")
            listo=[i.lower().capitalize() for i in _lst]
            _=horoscope(" ".join(listo)).get_daily()
            context.bot.send_message(chat_id=update.effective_chat.id,text=_)
        except KeyError:
            context.bot.send_message(chat_id=update.effective_chat.id,text="Arıes,Taurus,Gemını,Cancer,Leo,Virgo,Libra,Scorpio,Sagittarius,Capricorn,aquarius,pısces")
    def meme(self,update,context):
        _=reddit(info.password,info.username).get_meme()
        context.bot.send_photo(chat_id=update.effective_chat.id,photo=_)

    def gif(self,update,context):
        _=reddit(info.password,info.username).get_gif()
        context.bot.send_video(chat_id=update.effective_chat.id,video=_)

    def pandemic(self,update,context):
        chat_message=update.message.text
        _lst=chat_message.split(" ")
        _lst.remove("/pandemic")

        listo=[i.lower().capitalize() for i in _lst]
        _content="".join(listo)

        if 4 > len(_content) > 1:
            _context = _content.upper()
        if len(_lst)<1:
            _=hot_corona().get_country_case("World")
        else:       
            _=hot_corona().get_country_case(_context)

        context.bot.send_message(chat_id=update.effective_chat.id,text=_)

    def corona(self,update,context):
        chat_message=update.message
        _txt=chat_message.text
        a=_txt.split(" ")
        a.remove("/corona")
        hot_corona().plot("".join(a))
        _photo=hot_corona().upload_cloud()
        time.sleep(5)
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=_photo)
            
    def kick(self,update,context):
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
            
    def github(self,update,context):
        context.bot.send_message(chat_id=update.effective_chat.id,text=info._github)

    def help(self,update,context):
        context.bot.send_message(chat_id=update.effective_chat.id,text=info._help)
        
class group(functs):
    def __init__(self,updater,dp):
        super().__init__(updater,dp)

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
            

















            