from aiogram import Bot,Dispatcher,executor,types
import requests
import time
import logging
url="https://api.telegram.org/bot1085712406:AAHQfcaghrszrSAXCUtS7HGv3xYROyAPBBw/"
token="1085712406:AAHQfcaghrszrSAXCUtS7HGv3xYROyAPBBw"

bot=Bot(token=token)
dp=Dispatcher(bot)

osman=types.chat_member.ChatMember()
#print(osman.status)

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends /start or /help command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

if __name__ == 'main':
    executor.start_polling(dp, skip_updates=True)