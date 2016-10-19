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

def food(bot, update):
    food = prtFood(mensa.today('food'), 'Hauptgerichte')
    bot.sendMessage(update.message.chat_id, text=food, parse_mode = telegram.ParseMode.MARKDOWN)

def starters(bot, update):
    starters = prtFood(mensa.today('starters'), 'Vorspeisen')
    bot.sendMessage(update.message.chat_id, text=starters, parse_mode = telegram.ParseMode.MARKDOWN)

def salads(bot, update):
    salads = prtFood(mensa.today('salads'), 'Salate')
    bot.sendMessage(update.message.chat_id, text=salads, parse_mode = telegram.ParseMode.MARKDOWN)

def soups(bot, update):
    soups = prtFood(mensa.today('soups'), 'Suppen')
    bot.sendMessage(update.message.chat_id, text=soups, parse_mode = telegram.ParseMode.MARKDOWN)

def side_dishes(bot, update):
    side_dishes = prtFood(mensa.today('side_dishes'), 'Beilagen')
    bot.sendMessage(update.message.chat_id, text=side_dishes, parse_mode = telegram.ParseMode.MARKDOWN)

def special(bot, update):
    special = prtFood(mensa.today('special'), 'Aktionsstand')
    bot.sendMessage(update.message.chat_id, text=special, parse_mode = telegram.ParseMode.MARKDOWN)

def desserts(bot, update):
    desserts = prtFood(mensa.today('desserts'), 'Desserts')
    bot.sendMessage(update.message.chat_id, text=desserts, parse_mode = telegram.ParseMode.MARKDOWN)

def all(bot, update):
	food(bot, update)
	starters(bot, update)
	soups(bot, update)
	salads(bot, update)
	side_dishes(bot, update)
	special(bot, update)
	desserts(bot, update)

updater = Updater(token)
dp = updater.dispatcher
dp.add_handler(MessageHandler([Filters.text], all))
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("food", food))
dp.add_handler(CommandHandler("starters", starters))
dp.add_handler(CommandHandler("soups", soups))
dp.add_handler(CommandHandler("salads", salads))
dp.add_handler(CommandHandler("side_dishes", side_dishes))
dp.add_handler(CommandHandler("desserts", desserts))
dp.add_handler(CommandHandler("special", special))
dp.add_handler(CommandHandler("all", all))

updater.start_polling()
updater.idle()