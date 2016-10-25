import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from time import sleep
import mensa

token = open('token').read()
bot = telegram.Bot(token = token)

def prtFood(today, type):
    food = '*' + type + ':*\n'
    for n, val in enumerate(today):
        food += today[n]['Name'] + ':\n' + '    _' + today[n]['Price'] + '_\n'
    return food    

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi! You can use this bot to check the menue of the TU Mensa (Hardenbergstrasse).\n/food\n/starters\n/soups\n/salads\n/side_dishes\n/special\n/desserts')

def all(bot, update):
	food(bot, update)
	starters(bot, update)
	soups(bot, update)
	salads(bot, update)
	side_dishes(bot, update)
	special(bot, update)
	desserts(bot, update)

def functionify(type, name):
	return lambda bot, update: bot.sendMessage(update.message.chat_id, text=prtFood(mensa.today(type), name), parse_mode = telegram.ParseMode.MARKDOWN)

updater = Updater(token)
dp = updater.dispatcher
dp.add_handler(MessageHandler([Filters.text], all))
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("food", functionify('food', 'Hauptgerichte')))
dp.add_handler(CommandHandler("starters", functionify('starters', 'Vorspeisen')))
dp.add_handler(CommandHandler("soups", functionify('soups', 'Suppen')))
dp.add_handler(CommandHandler("salads", functionify('salads', 'Salate')))
dp.add_handler(CommandHandler("side_dishes", functionify('side_dishes', 'Beilagen')))
dp.add_handler(CommandHandler("desserts", functionify('desserts', 'Nachspeisen')))
dp.add_handler(CommandHandler("special", functionify('special', 'Aktionsstand')))
dp.add_handler(CommandHandler("all", all))

updater.start_polling()
updater.idle()