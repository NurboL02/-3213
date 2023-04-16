from telebot import types

from main import bot
import configure


@bot.message_handler(commands=['get_info', 'info'])
def send_welcome(message):
    markup_inline=types.InlineKeyboardMarkup
    item_yes = types.types.InlineKeyboardButton(text='Yes', callback_data='Da')
    item_no=types.InlineKeyboardButton(text='No', callback_data='Net')
    markup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, 'Желаете узнать о нашей пицерии',
      reply_markup=markup_inline)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Yes":
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_username=types.KeyboardButton('PIZZA')
        item_sushi=types.KeyboardButton('Sushi')
        markup_reply.add(item_sushi, item_username)
        bot.send_message(call.message.chat.id, 'Choose',
          reply_markup=markup_reply,)
    elif call.data == 'No':
        pass
@bot.message_handler(content_types=['text'])
def get_text(message):
    if message == 'PIZZA':
        bot.send_message(message.chad.usename, f'Пеперони\n Охотничая пицца')
    elif message.text=='Sushi':
        bot.send_message(message.chat.id,'Острые Суши \n Добрые суши')





