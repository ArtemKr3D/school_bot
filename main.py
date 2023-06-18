import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# bot = telebot.TeleBot('5596628205:AAH1lUAe11kJ4CfVHcg7d35qtxxXIf8O6a8')#prod
bot = telebot.TeleBot('6200157896:AAEewNsZ5Vv-7gq39uEf2oIwcyqMCPybB3k')  # test


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Доброго дня! 😁.')
    bot.send_message(message.chat.id, 'Ви знаєте хто я? /No /Yes')


@bot.message_handler(commands=['No'])
def no(message):
    bot.send_message(message.chat.id, 'Тоді я розповім 😊.')
    bot.send_message(message.chat.id,
                     'Я телеграм бот за допомогою якого ви можете замовити ручку та якісь констовари які я можу вам надати 😎.')
    bot.send_message(message.chat.id,
                     'Тепер ви знаєте хто я 🤗. Для детальнішої інформаці ви можете зателефонувати оператору 😉. /help')


@bot.message_handler(commands=['Yes'])  # TODO додати команду спонсор
def yes(message):
    bot.send_message(message.chat.id, 'Тоді Давайте розпочинати роботу 😁.')
    bot.send_message(message.chat.id, 'команди чата:')
    bot.send_message(message.chat.id, '/start - розпочати 🏁')
    bot.send_message(message.chat.id, '/help - команди чата ❓')
    bot.send_message(message.chat.id, '/buy - купити 💵')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'команди чата:')
    bot.send_message(message.chat.id, '/start - розпочати 🏁')
    bot.send_message(message.chat.id, '/help - команди чата ❓')
    bot.send_message(message.chat.id, '/buy - купити 💵')
    bot.send_message(message.chat.id, '/to_sponsor - стати моїм спонсором 💸')


@bot.message_handler(commands=['to_sponsor'])
def toSponsor(message):
    bot.send_message(message.chat.id, 'Дякую що ви хочете стати моїм спонсором 🥰')


@bot.message_handler(commands=['buy'])
def buy(message):
    button1 = InlineKeyboardButton(text="ручка-стирачка", callback_data="test1")
    button2 = InlineKeyboardButton(text='стержні до ручки стирачки', callback_data="test2")

    markup = InlineKeyboardMarkup()
    markup.add(button1, button2)

    bot.send_message(message.from_user.id, "виберіть товар:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "test1")
def test1(call):
    bot.send_message(call.message.chat.id, 'test11')


@bot.callback_query_handler(func=lambda call: call.data == "test2")
def test2(call):
    bot.send_message(call.message.chat.id, 'test22')


bot.polling(none_stop=True)
