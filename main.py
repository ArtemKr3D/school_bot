import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# bot = telebot.TeleBot('5596628205:AAH1lUAe11kJ4CfVHcg7d35qtxxXIf8O6a8')#prod
bot = telebot.TeleBot('6200157896:AAEewNsZ5Vv-7gq39uEf2oIwcyqMCPybB3k')  # test


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Доброго дня! 😁.')

    button1 = InlineKeyboardButton(text="так", callback_data="так")
    button2 = InlineKeyboardButton(text='ні', callback_data="ні")

    markup = InlineKeyboardMarkup()
    markup.add(button1, button2)

    bot.send_message(message.from_user.id, "Ви знаєте хто я?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "так")
def test1(call):
    button1 = InlineKeyboardButton(text="команди чата", callback_data="команди чата")

    markup = InlineKeyboardMarkup()
    markup.add(button1)

    bot.send_message(call.from_user.id, "Тоді Давайте розпочинати роботу 😁.", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "ні")
def test2(call):
    bot.send_message(call.message.chat.id, 'Тоді я розповім 😊.')
    bot.send_message(call.message.chat.id,
                     'Я телеграм бот за допомогою якого ви можете замовити ручку та якісь констовари які я можу вам надати 😎.')
    bot.send_message(call.message.chat.id,
                     'Тепер ви знаєте хто я 🤗. Для детальнішої інформаці ви можете зателефонувати оператору 😉.')

    button1 = InlineKeyboardButton(text="команди чата", callback_data="команди чата")

    markup = InlineKeyboardMarkup()
    markup.add(button1)

    bot.send_message(call.from_user.id, "Давайте розпочинати роботу 😁.", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "розпочати")
def test1(call):
    button1 = InlineKeyboardButton(text="так", callback_data="так")
    button2 = InlineKeyboardButton(text='ні', callback_data="ні")

    markup = InlineKeyboardMarkup()
    markup.add(button1, button2)

    bot.send_message(call.from_user.id, 'Доброго дня! 😁.')
    bot.send_message(call.from_user.id, "Ви знаєте хто я?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "команди чата")
def test1(call):
    button1 = InlineKeyboardButton(text="розпочати", callback_data="розпочати")
    button2 = InlineKeyboardButton(text="команди чата", callback_data="команди чата")
    button3 = InlineKeyboardButton(text="купити", callback_data="купити")
    markup = InlineKeyboardMarkup()
    markup.add(button1, button2, button3)

    bot.send_message(call.from_user.id, "команди чата", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "купити")
def test1(call):
    button1 = InlineKeyboardButton(text="ручка-стирачка", callback_data="ручка-стирачка")
    button2 = InlineKeyboardButton(text='стержні до ручки стирачки', callback_data="стержні до ручки стирачки")

    markup = InlineKeyboardMarkup()
    markup.add(button1, button2)

    bot.send_message(call.from_user.id, "виберіть товар:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "ручка-стирачка")
def test1(call):
    bot.send_photo(call.message.chat.id, photo=open('images/pen1.jpg', 'rb'))
    bot.send_message(call.message.chat.id, 'немає в наявності')


@bot.callback_query_handler(func=lambda call: call.data == "стержні до ручки стирачки")
def test2(call):
    bot.send_photo(call.message.chat.id, photo=open('images/15075389.jpg', 'rb'))
    bot.send_message(call.message.chat.id, 'немає в наявності')


bot.polling(none_stop=True)
