import telebot
from telebot import types
bot = telebot.TeleBot('');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    mes = message.text
    mes = mes.lower()
    if mes == "привет" or mes == ("qq"):
        bot.send_message(message.from_user.id, "зарегистрируйся) напиши /reg")
    elif message.text == '/start':
        bot.send_message(message.from_user.id, "Ну привет, новый пользователь) Скажи привет")
    elif mes == 'погода':
        bot.send_message(message.from_user.id, "Смотри погоду) \n https://www.ventusky.com/")
    elif mes == 'тревога':
        bot.send_message(message.from_user.id, "Вот карта тревог \n https://alarmmap.online/")
    elif mes == "/info":
        photo = open("C:\\Users\\chere\\Downloads\\KV-2.jpg", "rb")
        bot.send_photo(message.from_user.id, photo, caption = "Меня зовут КВ-2(не знаю почему авто меня так назвал). В общем-то КВ-2 это танк начала 2 мировой войны, у которого была громнейшая пушка 152 мм. Дальше информация из википедии: https://uk.wikipedia.org/wiki/КВ-2")
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Не плохо было бы и поздороваться, написать ПРИВЕТ хотя бы. \n \nЕсли хочешь узнать обо мне, напиши /info \n \n Если хочешь узнать погоду - напиши \n Погода \n \n Если хочешь узнать где сейчас тревога - напиши \n Тревога")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

name = ''
surname = ''
age = 0
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')
def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
        keyboard.add(key_yes); #добавляем кнопку в клавиатуру
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
        keyboard.add(key_no);
        question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?';
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if call.data == "yes":
                bot.send_message(call.message.chat.id, 'Запомню : )');
            elif call.data == "no":
                bot.send_message(call.message.chat.id, 'Начни регистрацию с начала')
bot.polling(none_stop=True, interval=0)