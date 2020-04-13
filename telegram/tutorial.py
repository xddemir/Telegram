import requests as requests
import random


url="https://api.telegram.org/bot1085712406:AAHQfcaghrszrSAXCUtS7HGv3xYROyAPBBw/"

# create func that get chat id
def get_chat_id(update):
    chat_id=update['message']["chat"]["id"]
    print(update)
    return chat_id

# create function that get message bot
def get_message_text(update):
    message_text=update["message"]["text"]
    return message_text

#create function that get_last_update
def last_update(req):
    response=requests.get(req+"getUpdates")
    response=response.json()
    result=response["result"]
    print(result)
    print(req)
    #result=response["result"]
    total_updates=len(result)-1
    return result[total_updates] # get last record message update

# create function that  let bot send message to user
def send_message(chat_id,message_text):
    params={"chat_id":chat_id,"text":message_text}
    response=requests.post(url+"sendMessage",data=params)
    return response

# create main function for navigate or reply message back
def main():
    update_id=last_update(url)["update_id"]
    print(update_id)
    while True:
        update=last_update(url)
        if update_id==update["update_id"]:
            if get_message_text(update).lower()=="hi"or get_message_text(update).lower()=="hello":
                send_message(get_chat_id(update),'Hello Welcome to our bot. Type "Play" to roll the dice!')
            elif get_message_text(update).lower()=="play":
                randm=random.randint(1,6)
                randm2=random.randint(1,6)
                randm3=random.randint(1,6)
                send_message(get_chat_id(update),"You have"+str(randm)+'and ' + str(randm2) + 'and '+str(randm3)+'!\n You result is' + str(randm+randm2+randm3) + "!!!")
            else:
                send_message(get_chat_id(update),"Sorry Not understand what you inputtend :(")               
            update_id+=1

 

#call the function to make it reply
#main()












