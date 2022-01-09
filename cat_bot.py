import requests
from telebot import *

bot = telebot.TeleBot("5051784869:AAEL3bORV78MzH27KUg8qRCLIe-2ADcQJSg")


@bot.message_handler(commands=['cat'])
def api_cat(message):  
    url = "https://thatcopy.pw/catapi/rest/"
    r = requests.get(url)
    data = r.json()
    bot.send_photo(message.chat.id, data['url'])
    print("Link: ", data['url'])

bot.polling()