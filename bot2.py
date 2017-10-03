import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from time import sleep
import mensa2

token = open('token').read()
bot = telegram.Bot(token = token)

def prtFood(entries, type):
    food = '*' + type + ':*\n'
    for entry in entries:
        food += entry + '\n'
    return food    

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi! Mithilfe dieses Bots kannst Du den Speiseplan der TU Mensa (Hardenbergstrasse) abrufen.\n/Essen\n/Vorspeisen\n/Suppen\n/Salate\n/Beilagen\n/Aktionen\n/Desserts\n/Speiseplan')

def all(bot, update):
	(functionify('Essen'))(bot, update)
	(functionify('Vorspeisen'))(bot, update)
	(functionify('Suppen'))(bot, update)
	(functionify('Salate'))(bot, update)
	(functionify('Beilagen'))(bot, update)
	(functionify('Desserts'))(bot, update)
	(functionify('Aktionen'))(bot, update)

def functionify(type):
	return lambda bot, update: bot.sendMessage(update.message.chat_id, text=prtFood(mensa2.food()[type], type), parse_mode = telegram.ParseMode.MARKDOWN)

updater = Updater(token)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("Essen", functionify('Essen')))
dp.add_handler(CommandHandler("Vorspeisen", functionify('Vorspeisen')))
dp.add_handler(CommandHandler("Suppen", functionify('Suppen')))
dp.add_handler(CommandHandler("Salate", functionify('Salate')))
dp.add_handler(CommandHandler("Beilagen", functionify('Beilagen')))
dp.add_handler(CommandHandler("Desserts", functionify('Desserts')))
dp.add_handler(CommandHandler("Aktionen", functionify('Aktionen')))
dp.add_handler(CommandHandler("Speiseplan", all))

updater.start_polling()
updater.idle()