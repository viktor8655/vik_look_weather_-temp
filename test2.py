import telebot
from telebot import types
import requests
import json

bot = telebot.TeleBot('5680128942:AAGvcEmSyNObpoV9DyV4YyqsoGei1hanAsc')
API = '86e8cbac4d64f630c00a528611932773'


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'<b>Hello  {message.from_user.first_name}</b>  <u>write the name of the city</u>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        bot.reply_to(message, f"Now the weather:{temp}")

        image = 'sunny.jpeg' if 10.0 < temp > 10.0  else 'cold.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, " wrong city")


bot.polling(none_stop=True)