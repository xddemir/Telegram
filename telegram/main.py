import logging,info
import telegram
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,Handler
from telegram import ChatMember
from functs import functs,group

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def main():
    updater=Updater(token=info.token,use_context=True)
    dp=updater.dispatcher
## REFACTORING
    _function=functs(updater,dp)
    func_lst=[getattr(_function,x) for x in dir(_function) if not x.startswith("__")]
    func_names=[y for y in dir(functs(updater,dp)) if not y.startswith("__")]
    
    for i in range(len(func_lst)):
        dp.add_handler(CommandHandler(func_names[i],func_lst[i]))

    help("modules")
    """dp.add_handler(CommandHandler("help",functs(updater,dp).help_bot))
    dp.add_handler(CommandHandler("corona",functs(updater,dp).graph_pandemic))
    dp.add_handler(CommandHandler("youtube",functs(updater,dp).youtubeSearchSelenium))
    dp.add_handler(CommandHandler("currency",functs(updater,dp).currency_exchange))
    dp.add_handler(CommandHandler("movie",functs(updater,dp).imdbMovies))
    dp.add_handler(CommandHandler("word",functs(updater,dp).Vocabulary))
    dp.add_handler(CommandHandler("weather",functs(updater,dp).weather))
    dp.add_handler(CommandHandler("horos",functs(updater,dp).horoscope))
    dp.add_handler(CommandHandler("meme",functs(updater,dp).sendMessag))
    dp.add_handler(CommandHandler("gif",functs(updater,dp).sendGif))
    dp.add_handler(CommandHandler("pandemic",functs(updater,dp).sendPandemic))
    dp.add_handler(CommandHandler("kick",functs(updater,dp).kick_member))"""

    dp.add_handler(MessageHandler(Filters.text,group(updater,dp).remove_forbidden_words))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members,group(updater,dp).welcome_member))
    
    updater.start_polling()
    updater.idle()


if __name__=='__main__':
    print("i am running!")
    main()
