import telebot

bot = telebot.TeleBot('5596628205:AAH1lUAe11kJ4CfVHcg7d35qtxxXIf8O6a8')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'test start command')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'test help command')

bot.polling(none_stop=True)
