import requests
import time
import logging
import telegram
from bs4 import BeautifulSoup
from movie import imdbMovie
from vocabulary import Vocab
from weather import weathers
######################################33
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import ChatMember
################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url="https://api.telegram.org/bot1208256641:AAGBZdWu3UeXzQoF2wzTfgNLtRtj34ElHwE/"
token="1208256641:AAGBZdWu3UeXzQoF2wzTfgNLtRtj34ElHwE"
bot = telegram.Bot(token=token)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
############################################################################################################
def get_Chat_id(url):
    req=requests.get(url+"getUpdates")
    response=req.json()
    items=response["result"]
    lst_update=items[get_Last_Update(url)]
    return lst_update["channel_post"]["chat"]["id"]

def get_Last_Update(url):
     req=requests.get(url+"getUpdates")
     response=req.json()
     update_lenght=len(response["result"])-1
     return update_lenght
 
def get_message(url):
    req=requests.get(url+"getUpdates")
    response=req.json()
    _id=get_Last_Update(url)
    text=response["result"][_id]['channel_post']['text']
    return text

def get_message_id(url):
    req=requests.get(url+"getUpdates")
    response=req.json()
    last_update=get_Last_Update(url)
    result=response["result"]
    return result[last_update]['message']['message_id']

def send_message(chat_id,message_text,url):
    params={
        "chat_id":chat_id,
        "text":message_text,
    }
    response=requests.post(url+"sendMessage",data=params)
    return response

    #requests.get(url+f"sendMessage?chat_id={chat_id}&text={message})
# 828771246 from chat id
def forwardMessage(url):
    chat_id=get_Chat_id(url)
    from_chat_id="828771246"
    message_id=get_message_id(url)
    response=requests.post(url+"forwardMessage",params={
        "chat_id":chat_id,
        "from_chat_id":from_chat_id,
        "message_id":message_id
    })
    return response
def sendChatAction(url):
    chat_id=get_Chat_id(url)
    action="typing.."
    response=requests.get(url+"sendChatAction",params={
        "chat_id":chat_id,
        "action":action
    })
    return response
#############################################################################################################



def currency_exchange(update,context):
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

def youtubeSearchSelenium(update,context):
        _url="https://www.youtube.com/"
        _msg=update.message.text
        msg_lst=_msg.split(" ")
        msg=msg_lst[1]
        #if get_message(url)==f"/youtube {msg}":
        driver=webdriver.Firefox()
        new_url=f"{_url}results?search_query={msg}"
        driver.get(new_url)
        elem=driver.find_element_by_xpath("//*[@id='thumbnail']").get_attribute("href")
        time.sleep(1)
        context.bot.send_message(chat_id=update.effective_chat.id,text=elem)
        #send_message(get_Chat_id(url),elem,url)

def start(update,context): # it gives user id
    chat_user=20200410232728#1208256641
    _user=telegram.ChatMember(chat_user,"online")
    print(update._effective_user)
    
def imdbMovies(update,context):
    chat_message=update.message.text
    _list=chat_message.split(" ")
    _list.remove("/movie")
    x=imdbMovie("".join(_list)).get_movie()
    context.bot.send_message(chat_id=update.effective_chat.id,text=x)

def Vocabulary(update,context):
    try:
        chat_message=update.message.text
        x=Vocab(chat_message).mean()
        context.bot.send_message(chat_id=update.effective_chat.id,text=x)
    except KeyError:
        context.bot.send_message(chat_id=update.effective_chat.id,text="İnvaild Syntax :(")

def weather(update,context):
    try:
        chat_message=update.message.text
        _lst=chat_message.split(" ")
        _lst.remove("/weather")
        _=weathers("".join(_lst)).get_location()
        context.bot.send_message(chat_id=update.effective_chat.id,text=_)
    except KeyError:
        context.bot.send_message(chat_id=update.effective_chat.id,text="İnvaild Syntax :(")
        
        

def main():
    updater=Updater(token=token,use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("youtube",youtubeSearchSelenium))
    dp.add_handler(CommandHandler("currency",currency_exchange))
    dp.add_handler(CommandHandler("movie",imdbMovies))
    dp.add_handler(CommandHandler("word",Vocabulary))
    dp.add_handler(CommandHandler("weather",weather))
    
    #hello
    updater.start_polling()
    updater.idle()
   

#print(send_message(get_Chat_id(url),"hello",url))

if __name__=='__main__':
    print("i am running!")
    main()
