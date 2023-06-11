import telebot

bot = telebot.TeleBot('5596628205:AAH1lUAe11kJ4CfVHcg7d35qtxxXIf8O6a8')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Зроблю незвичайну Заставку на meet та google. 1 грн одна заставка. /help ❓ ')

bot.polling(none_stop=True)