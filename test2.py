import telebot
from telebot import types

bot = telebot.TeleBot('5680128942:AAGvcEmSyNObpoV9DyV4YyqsoGei1hanAsc')
API = '86e8cbac4d64f630c00a528611932773'


""" bot for checking weather """

text = 'hi'

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'<b>Hello  {message.from_user.first_name}</b>  <u>enter command /time</u>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True)