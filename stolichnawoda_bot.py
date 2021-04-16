# -*- coding: utf-8 -*-
import telebot
from telebot import types # кнопки
from string import Template

bot = telebot.TeleBot('Ваш Токен')

user_dict = {}

class User:
    def __init__(self, city):
        self.city = city

        keys = ['fullname', 'phone', 'driverSeria', 
                'driverNumber']
        
        for key in keys:
            self.key = None

# если /start
@bot.message_handler(commands=['start', 'help'])
def start(message):
    #create buttons
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Заказать Воду🌊')
    btn2 = types.KeyboardButton('О нас❗')
    btn3 = types.KeyboardButton('Акции✨')
    btn4 = types.KeyboardButton('Контакти☎')
    markup.add(btn1,btn2,btn3, btn4)

    #Text start
    bot.send_message(message.chat.id, "Здравствуйте "
    + message.from_user.first_name
    + ", я Ваш персональный асиситент😊\n\nС помощью меня, Вы можете:\n\
✅Сделать заказ воды.\n✅Связаться с диспетчером.\n✅Узнать про Акции.", reply_markup=markup, parse_mode='html')



@bot.message_handler(content_types=['text'])
# Принятие заявки на доставку 
def user_reg(message):
    if message.text == 'Заказать Воду🌊':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Киев')
        itembtn2 = types.KeyboardButton('Главное меню⚡')
        markup.add(itembtn1, itembtn2)

        msg = bot.send_message(message.chat.id, '*Ваш город?*', reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(msg, process_city_step)
    
    #Остальные кнокпи
    elif message.text == 'О нас❗':
    	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    	btn1 = types.KeyboardButton('Контакти☎')
    	btn2 = types.KeyboardButton('График работы💡')
    	btn3 = types.KeyboardButton('Главное меню⚡')
    	markup.add(btn1, btn2, btn3)
    	bot.send_message(message.chat.id, 'Специалисты нашей компании с 2000 года профессионально занимаются производством и доставкой бутылированной воды в г. Киеве.', reply_markup=markup)
    
    elif message.text	 == 'Главное меню⚡':
    	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    	btn1 = types.KeyboardButton('Заказать Воду🌊')
    	btn2 = types.KeyboardButton('О нас❗')
    	btn3 = types.KeyboardButton('Акции✨')
    	btn4 = types.KeyboardButton('Контакти☎')
    	markup.add(btn1, btn2, btn3, btn4)
    	bot.send_message(message.chat.id,'Выберите категорию', reply_markup=markup)
    
    elif message.text == 'Контакти☎':
    	markup = types.ReplyKeyboardMarkup(one_time_keyboard= True, resize_keyboard=True, row_width=2)
    	marku = types.InlineKeyboardMarkup(row_width=2)
    	btn1 = types.KeyboardButton('Заказать Воду🌊')
    	btn2 = types.KeyboardButton('О нас❗')
    	btn3 = types.KeyboardButton('Акции✨')
    	markup.add(btn1, btn2, btn3)
    	firs_button = types.InlineKeyboardButton(text="Telegramm", url = "https://t.me/stolichnavoda")
    	marku.add(firs_button)
    	send_mess7 = "*Прием заказов:*\nДиспетчером шесть дней в неделю с *9:00* до *18:00*, в остальное время можно сделать заказ в Viber, Telegramm.\n\n\
📞*(063)599-77-11*\n📞*(044)599-77-11*\n✉*vodastolichna@gmail.com*"

    	bot.send_message(message.chat.id, send_mess7, reply_markup=markup and marku,  parse_mode=('Markdown','html'))

    elif message.text == 'График работы💡':
    	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    	btn3 = types.KeyboardButton('Главное меню⚡')
    	markup.add(btn3)
    	send_mess8 = 'Доставка осуществляется шесть дней в неделю с *7:00* до *18:00*. Без ограничения по времени.\nВоскресенье – выходной день.\n\n\
Выполнение заказов «день в день» при наличии технической возможности.\n\n*Минимальный заказ – 2 бутыля.*'

    	bot.send_message(message.chat.id, send_mess8, reply_markup=markup, parse_mode="Markdown")

    elif message.text == 'Акции✨':
    	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    	btn1 = types.KeyboardButton('Заказать Воду🌊')
    	btn2 = types.KeyboardButton('О нас❗')
    	btn3 = types.KeyboardButton('Акции✨')
    	btn4 = types.KeyboardButton('Контакти☎')
    	markup.add(btn1, btn2, btn3, btn4)
    	fille_1 = open('C:/Users/38063/Desktop/Bot_telegram/hj.jpg' , 'rb')
    	fille_2 = open('C:/users/38063/Desktop/Bot_telegram/nn.jpg', 'rb')

    	bot.send_photo(message.chat.id, fille_2 , '*При заказе 5 бутылей - скидка - 50% на стойку для бутылей*',reply_markup=markup, parse_mode= "Markdown")
    	bot.send_photo(message.chat.id, fille_1, '*При заказе трех бутылей - Помпа в подарок*', reply_markup=markup, parse_mode= "Markdown")
    	send_mess5 = '*Условия получения:*\n\n*1.* Первый заказ в нашей компании.\n*2.* Минимальное количество бутылей в заказе — 3бут/5бут соответственно.\n*3.* Внесение залога за каждый PC бутыль в заказе. Стоимость одного бутыля — 140грн. Подлежит возврату.'
    	bot.send_message(message.chat.id, send_mess5, reply_markup=markup, parse_mode='Markdown')

 
 #Продолжение регистрации 
def process_city_step(message):
	if message.text	 == 'Главное меню⚡':
		markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('Заказать Воду🌊')
		btn2 = types.KeyboardButton('О нас❗')
		btn3 = types.KeyboardButton('Акции✨')
		btn4 = types.KeyboardButton('Контакти☎')
		markup.add(btn1, btn2, btn3, btn4)
		bot.send_message(message.chat.id,'Выберите категорию', reply_markup=markup)
	else:
		try:
			chat_id = message.chat.id
			user_dict[chat_id] = User(message.text)

        	# удалить старую клавиатуру
			markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
			btn1= types.KeyboardButton('Главное меню⚡')
			markup.add(btn1)

			msg = bot.send_message(chat_id, '*Ф.И.О*', reply_markup=markup, parse_mode="Markdown")
			bot.register_next_step_handler(msg, process_fullname_step)

		except Exception as e:
			bot.reply_to(message, 'ooops!!')

def process_fullname_step(message):
    if message.text	 == 'Главное меню⚡':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Заказать Воду🌊')
        btn2 = types.KeyboardButton('О нас❗')
        btn3 = types.KeyboardButton('Акции✨')
        btn4 = types.KeyboardButton('Контакти☎')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id,'Выберите категорию', reply_markup=markup)
    else:
        try:
            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.fullname = message.text

            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            btn1= types.KeyboardButton('Главное меню⚡')
            markup.add(btn1)

            msg = bot.send_message(chat_id, '*Ваш номер телефона*', parse_mode="Markdown")
            bot.register_next_step_handler(msg, process_phone_step)

        except Exception as e:
            bot.reply_to(message, 'ooops!!')

def process_phone_step(message):
    if message.text	 == 'Главное меню⚡':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Заказать Воду🌊')
        btn2 = types.KeyboardButton('О нас❗')
        btn3 = types.KeyboardButton('Акции✨')
        btn4 = types.KeyboardButton('Контакти☎')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id,'Выберите категорию', reply_markup=markup)
    else:
        try:
            int(message.text)

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.phone = message.text

            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            btn1= types.KeyboardButton('Главное меню⚡')
            markup.add(btn1)

            msg = bot.send_message(chat_id, '*Адрес доставки* (улица, номер дома, квартира, подъезд)', parse_mode="Markdown")
            bot.register_next_step_handler(msg, process_Adres_step)

        except Exception as e:
            msg = bot.reply_to(message, 'Вы ввели что то другое. Пожалуйста введите номер телефона.')
            bot.register_next_step_handler(msg, process_phone_step)

def process_Adres_step(message):
    if message.text	 == 'Главное меню⚡':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Заказать Воду🌊')
        btn2 = types.KeyboardButton('О нас❗')
        btn3 = types.KeyboardButton('Акции✨')
        btn4 = types.KeyboardButton('Контакти☎')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id,'Выберите категорию', reply_markup=markup)
    else:
        try:
            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.driverSeria = message.text

            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            btn1= types.KeyboardButton('Главное меню⚡')
            markup.add(btn1)

            msg = bot.send_message(chat_id, '*Количество бутылей*', parse_mode="Markdown" )
            bot.register_next_step_handler(msg, process_Botle_step)

        except Exception as e:
            bot.reply_to(message, 'ooops!!')

def process_Botle_step(message):
    if message.text	 == 'Главное меню⚡':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Заказать Воду🌊')
        btn2 = types.KeyboardButton('О нас❗')
        btn3 = types.KeyboardButton('Акции✨')
        btn4 = types.KeyboardButton('Контакти☎')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id,'Выберите категорию', reply_markup=markup)

    elif int(message.text) >= int(2):

        chat_id = message.chat.id
        user = user_dict[chat_id] 
        user.driverNumber = message.text

        grn = int(message.text)
        grn1 = int(0)
        for i in range(grn):
            grn1 +=70
        grn2 = str(grn1)
        
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Заказать Воду🌊')
        btn2 = types.KeyboardButton('О нас❗')
        btn3 = types.KeyboardButton('Акции✨')
        btn4 = types.KeyboardButton('Контакти☎')
        markup.add(btn1, btn2, btn3, btn4)

        msg = getRegData(user, 'Ваша заявка', message.from_user.first_name)
        # ваша заявка "Имя пользователя"
        bot.send_message(chat_id, msg, reply_markup=markup,  parse_mode="Markdown")
        msg1 = bot.send_message(message.chat.id, f'Сумма к оплате: *{grn2} гривен*', parse_mode ='Markdown')
        # отправить в группу
        bot.send_message(id_group, getRegData(user, 'Заявка от бота', bot.get_me().username),  parse_mode="Markdown")

    else:
        msg = bot.reply_to(message, 'Минимальный заказ, 2 бутыля.')
        bot.register_next_step_handler(msg, process_Botle_step)

    # формирует вид заявки регистрации
    # нельзя делать перенос строки Template
    # в send_message должно стоять parse_mode="Markdown"
def getRegData(user, title, name):
    t = Template('$title *$name* \n Город: *$userCity* \n ФИО: *$fullname* \n Телефон: *$phone* \n Адрес доставки: *$driverSeria* \n Количество бутылей: *$driverNumber*')

    return t.substitute({
        'title': title,
        'name': name,
        'userCity': user.city,
        'fullname': user.fullname,
        'phone': user.phone,
        'driverSeria': user.driverSeria,
        'driverNumber': user.driverNumber,
    })

bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()


if __name__ == '__main__':
    bot.polling(none_stop=True)
