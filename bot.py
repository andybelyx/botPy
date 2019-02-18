import telebot


bot = telebot.TeleBot("yuor_token")


@bot.message_handler(commands=["start"])
def hendle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard='True');
    user_markup.row('ДА')
    user_markup.row('ОЧЕНЬ')
    user_markup.row('НЕТ')
    bot.send_message(message.chat.id,'Добро пожаловать! Вы любите кино ' + message.from_user.first_name , reply_markup=user_markup)

@bot.message_handler(regexp="ДА")
def geophone(message):
    bot.send_message(message.chat.id, "ОТЛИЧНО ВОТ ЛУЧШИЙ КИНОСАЙТ!! http://baskino.me/")

@bot.message_handler(regexp="ОЧЕНЬ")
def geophone(message):
    bot.send_message(message.chat.id, "ЮТУБ ССЫЛКА С ЛУЧШИМИ ПОДБОРКАМИ В СКОРОМ ВРЕМЕНИ!")


@bot.message_handler(regexp="НЕТ")
def geophone(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True,one_time_keyboard='True')
    button_phone = telebot.types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = telebot.types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, "Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!", reply_markup=keyboard)

	

bot.polling(none_stop=True, interval=0)
