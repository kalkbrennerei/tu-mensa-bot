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
    #bot.sendChatAction(update.message.chat_id, action=telegram.ChatAction.TYPING)
    return food    

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')

def food(bot, update):
    food = prtFood(mensa.food('food', 'today'), 'Hauptgerichte')
    bot.sendMessage(update.message.chat_id, text=food, parse_mode = telegram.ParseMode.MARKDOWN)

def starters(bot, update):
    starters = prtFood(mensa.food('starters', 'today'), 'Vorspeisen')
    bot.sendMessage(update.message.chat_id, text=starters, parse_mode = telegram.ParseMode.MARKDOWN)

def salads(bot, update):
    salads = prtFood(mensa.food('salads', 'today'), 'Salate')
    bot.sendMessage(update.message.chat_id, text=salads, parse_mode = telegram.ParseMode.MARKDOWN)

def soups(bot, update):
    soups = prtFood(mensa.food('soups', 'today'), 'Suppen')
    bot.sendMessage(update.message.chat_id, text=soups, parse_mode = telegram.ParseMode.MARKDOWN)

def side_dishes(bot, update):
    side_dishes = prtFood(mensa.food('side_dishes', 'today'), 'Beilagen')
    bot.sendMessage(update.message.chat_id, text=side_dishes, parse_mode = telegram.ParseMode.MARKDOWN)

def special(bot, update):
    special = prtFood(mensa.food('special', 'today'), 'Sonderangebote')
    bot.sendMessage(update.message.chat_id, text=special, parse_mode = telegram.ParseMode.MARKDOWN)

def desserts(bot, update):
    desserts = prtFood(mensa.food('desserts', 'today'), 'Desserts')
    bot.sendMessage(update.message.chat_id, text=desserts, parse_mode = telegram.ParseMode.MARKDOWN)

def all(bot, update):
	food(bot, update)
	starters(bot, update)
	soups(bot, update)
	salads(bot, update)
	side_dishes(bot, update)
	special(bot, update)
	desserts(bot, update)

def test(bot, update):
	bot.sendMessage(update.message.chat_id, text="```\nI'm sorry Dave I'm afraid I can't do that\n```", parse_mode = telegram.ParseMode.MARKDOWN)

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
dp.addHandler(CommandHandler("test", test))

updater.start_polling()
updater.idle()