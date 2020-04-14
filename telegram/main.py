import logging
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import ChatMember
from functs import functs
import info
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def main():
    updater=Updater(token=info.token,use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",functs(updater,dp).start))
    dp.add_handler(CommandHandler("youtube",functs(updater,dp).youtubeSearchSelenium))
    dp.add_handler(CommandHandler("currency",functs(updater,dp).currency_exchange))
    dp.add_handler(CommandHandler("movie",functs(updater,dp).imdbMovies))
    dp.add_handler(CommandHandler("word",functs(updater,dp).Vocabulary))
    dp.add_handler(CommandHandler("weather",functs(updater,dp).weather))
    
    updater.start_polling()
    updater.idle()


if __name__=='__main__':
    print("i am running!")
    main()
