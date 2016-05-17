import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from time import sleep
import mensa

token = open('token').read()

bot = telegram.Bot(token = token)

def prtFood(today, type):
    food = type + ':\n'
    for n, val in enumerate(today):
        food += today[n]['Name'] + today[n]['Price'] + '\n'
    return food    

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')

def food(bot, update):
    food = prtFood(mensa.food('food', 'today'), 'food')
    bot.sendMessage(update.message.chat_id, text=food)

def starters(bot, update):
    starters = prtFood(mensa.food('starters', 'today'), 'starters')
    bot.sendMessage(update.message.chat_id, text=starters)

def salads(bot, update):
    salads = prtFood(mensa.food('salads', 'today'), 'salads')
    bot.sendMessage(update.message.chat_id, text=salads)

def soups(bot, update):
    soups = prtFood(mensa.food('soups', 'today'), 'soups')
    bot.sendMessage(update.message.chat_id, text=soups)

def side_dishes(bot, update):
    side_dishes = prtFood(mensa.food('side_dishes', 'today'), 'side_dishes')
    bot.sendMessage(update.message.chat_id, text=side_dishes)

def special(bot, update):
    special = prtFood(mensa.food('special', 'today'), 'special')
    bot.sendMessage(update.message.chat_id, text=special)

def desserts(bot, update):
    desserts = prtFood(mensa.food('desserts', 'today'), 'desserts')
    bot.sendMessage(update.message.chat_id, text=desserts)

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
dp.addHandler(MessageHandler([Filters.text], all))
dp.addHandler(CommandHandler("start", start))
dp.addHandler(CommandHandler("food", food))
dp.addHandler(CommandHandler("starters", starters))
dp.addHandler(CommandHandler("soups", soups))
dp.addHandler(CommandHandler("salads", salads))
dp.addHandler(CommandHandler("side_dishes", side_dishes))
dp.addHandler(CommandHandler("desserts", desserts))
dp.addHandler(CommandHandler("special", special))
dp.addHandler(CommandHandler("all", all))

updater.start_polling()
updater.idle()

# while(True):
# 	updates = bot.getUpdates()
# 	for update in updates:
# 		chat_id = update.message.chat_id
# 		text = update.message.text
# 		bot.sendMessage(chat_id = chat_id, text = text)
# 	sleep(.3)