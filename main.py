import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('6590677711:AAHOBqyCFnW31xjUXOtIx-DeexpMVqbqCkQ') # prod

buttonYes = InlineKeyboardButton(text="так", callback_data="так")
buttonNo = InlineKeyboardButton(text='ні', callback_data="ні")

def lambda_handler(event, context):
    update = telebot.types.Update.de_json(event['body'])
    bot.process_new_updates([update])
    return {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Доброго дня! 😁.')

    markup = InlineKeyboardMarkup()
    markup.add(buttonYes, buttonNo)

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
                     'Я телеграм бот за допомогою якого ви можете переглядати розклад та інші можливості які я можу вам надати 😎.')
    bot.send_message(call.message.chat.id,
                     'Тепер ви знаєте хто я 🤗. Для детальнішої інформаці ви можете зателефонувати оператору 😉. +380 95 414 84 23📱')

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
    button3 = InlineKeyboardButton(text="розклад занять", callback_data="розклад занять")
    button4 = InlineKeyboardButton(text="соцмережі", callback_data="соцмережі")
    button5 = InlineKeyboardButton(text="допомога", callback_data="допомога")
    markup = InlineKeyboardMarkup()
    markup.add(button1, button2, button3, button4, button5)


    bot.send_message(call.from_user.id, "команди чата", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "розклад занять")
def test1(call):
    button1 = InlineKeyboardButton(text="Понеділок", callback_data="Понеділок")
    button2 = InlineKeyboardButton(text='Вівторок', callback_data="Вівторок")
    button3 = InlineKeyboardButton(text='Середа', callback_data="Середа")
    button4 = InlineKeyboardButton(text='Четвер', callback_data="Четвер")
    button5 = InlineKeyboardButton(text='П‘ятниця', callback_data="П‘ятниця")

    markup = InlineKeyboardMarkup()
    markup.row(button1, button2, button3, button4, button5)

    bot.send_message(call.from_user.id, "виберіть день:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "соцмережі")
def test1(call):
    bot.send_message(call.from_user.id, "соцмережі:")
    bot.send_message(call.from_user.id, "Телеграм💬: https://t.me/+xh1gfb8eoZ1mMjky")
    bot.send_message(call.from_user.id, "Інстаграм📷: https://www.instagram.com/school_bot_voice1/")


@bot.callback_query_handler(func=lambda call: call.data == "допомога")
def test1(call):

    bot.send_message(call.from_user.id, "Допоможи, купи мені кофе! https://www.buymeacoffee.com/artkravtsoe")


@bot.callback_query_handler(func=lambda call: call.data == "Понеділок")
def test1(call):
    bot.send_message(call.message.chat.id, '''Понеділок
5. Основи здоров’я (410)
6.Англійська ( каб. 403, 417)
7. Історія ( каб. 412)
8. Математика ( каб. 410)
9. Географія ( 407)
10. Інформатика ( каб. 44, 32)''')

@bot.callback_query_handler(func=lambda call: call.data == "Вівторок")
def test2(call):
    bot.send_message(call.message.chat.id, '''Вівторок
4. Укр. мова ( каб. 414)
5. Фізкультура
6. Технології 
7. Укр. літ. ( каб. 414)
8. Пізнаємо світ ( каб. 316)
9. Математика ( каб.210)
10. Англійська ( каб. 403, 417)''')

@bot.callback_query_handler(func=lambda call: call.data == "Середа")
def test2(call):
    bot.send_message(call.message.chat.id, '''Середа
4. Укр. мова 414
5. Математика (404)
6. Англійська ( 407,417)
7. Фізкультура
8. Інформатика ( каб. 44, 32)
9. Історія ( каб. 416)
10. Географія ( каб. 407)''')
#
@bot.callback_query_handler(func=lambda call: call.data == "Четвер")
def test2(call):
    bot.send_message(call.message.chat.id, '''Четвер
4. Мистецтво 215
5. Зарубіжна 410
6. Математика ( каб. 210).
7. Укр. мова ( каб. 414)
8. Укр. літ ( каб. 414)
9. Англійська ( каб. 403, 417)''')
#
@bot.callback_query_handler(func=lambda call: call.data == "П‘ятниця")
def test2(call):
    bot.send_message(call.message.chat.id, '''П‘ятниця
4. Зарубіжна ( 410)
5. Украінська мова (каб.414)
6. Англійська  ( каб. 403, 417)
7. Пізнаю світ ( 326)
8. Математика ( каб. 210)
9. Фізкультура''')


bot.polling(none_stop=True)
