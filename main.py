import telebot

bot = telebot.TeleBot('5596628205:AAH1lUAe11kJ4CfVHcg7d35qtxxXIf8O6a8')#prod
# bot = telebot.TeleBot('6200157896:AAEewNsZ5Vv-7gq39uEf2oIwcyqMCPybB3k')#test

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Доброго дня! 😁.')
    bot.send_message(message.chat.id, 'Ви знаєте хто я? /No /Yes')

@bot.message_handler(commands=['No'])
def main(message):
    bot.send_message(message.chat.id, 'Тоді я розповім 😊.')
    bot.send_message(message.chat.id, 'Я телеграм бот за допомогою якого ви можете замовити ручку та якісь констовари які я можу вам надати 😎.')
    bot.send_message(message.chat.id, 'Тепер ви знаєте хто я 🤗. Для детальнішої інформаці ви можете зателефонувати оператору 😉. /help')

@bot.message_handler(commands=['Yes'])
def main(message):
    bot.send_message(message.chat.id, 'Тоді Давайте розпочинати роботу 😁.')
    bot.send_message(message.chat.id, 'команди чата:')
    bot.send_message(message.chat.id, '/start - розпочати 🏁')
    bot.send_message(message.chat.id, '/help - команди чата ❓')
    bot.send_message(message.chat.id, '/buy - купити 💵')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'команди чата:')
    bot.send_message(message.chat.id, '/start - розпочати 🏁')
    bot.send_message(message.chat.id, '/help - команди чата ❓')
    bot.send_message(message.chat.id, '/buy - купити 💵')
    bot.send_message(message.chat.id, '/to_sponsor - стати моїм спонсором 💸')

@bot.message_handler(commands=['to_sponsor'])
def main(message):
    bot.send_message(message.chat.id, 'Дякую що ви хочете стати моїм спонсором 🥰')
    bot.send_message(message.chat.id, 'Дякую що ви хочете стати моїм спонсором 🥰')

@bot.message_handler(commands=['buy'])
def main(message):
    bot.send_message(message.chat.id, 'виберіть товар:')
    bot.send_message(message.chat.id, '/1 ручка-стирачка')
    bot.send_message(message.chat.id, '/2 стержні до ручки стирачки')

@bot.message_handler(commands=['1'])
def main(message):
    bot.send_message(message.chat.id, 'Я вибачаюся але це поки що неможливо ☹')
    bot.send_message(message.chat.id, '/help')

@bot.message_handler(commands=['2'])
def main(message):
    bot.send_message(message.chat.id, 'Я вибачаюся але це поки що неможливо ☹')
    bot.send_message(message.chat.id, '/help')

bot.polling(none_stop=True)
