from _ast import Pass
import telebot
from telebot import types
import configure

bot = telebot.TeleBot('6145140146:AAE-6nGJ1e_w57f1Ez1kZIk-Vwo3oexZPDs')

bot.polling(non_stop=True, interval=0)