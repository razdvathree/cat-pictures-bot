import requests
from telebot import *

token = "" #token from @BotFather

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['cat'])
def api_cat(message):  
    url = "https://thatcopy.pw/catapi/rest/"
    r = requests.get(url)
    data = r.json()
    bot.send_photo(message.chat.id, data['url'])
    print("Link: ", data['url'])

bot.polling()
