import telebot
from telebot import types
from bot_logic import gen_lot, vin_lot, mon, sm

vin_bil = vin_lot() 
my_bil = gen_lot()
money = mon()
smile = sm()

API_TOKEN = 'тут мой токен'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, добро пожаловать в бота! Введи команду /cmd')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/lot")
    item2 = types.KeyboardButton("/cmd")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Выберите команду:', reply_markup=markup)

@bot.message_handler(commands=['cmd'])
def cmd(message):
    bot.send_message(message.chat.id, 'Команды: /lot (Это лотерея, чтобы активировать введите эту команду).')
    
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Подбросить монету", callback_data='coin')
    button2 = types.InlineKeyboardButton("Выбрать рандомный смайлик", callback_data='smile')
    markup.add(button1, button2)
    
    bot.send_message(message.chat.id, 'Нажмите на кнопку:', reply_markup=markup)

@bot.message_handler(commands=['lot'])
def lot(message):
    global vin_bil, my_bil
    vin_bil = vin_lot()
    bot.send_message(message.chat.id, 'Выбираем рандомное выигрышное число...')
    bot.send_message(message.chat.id, f"Выигрышное число: {vin_bil}")
    
    my_bil = gen_lot()
    bot.send_message(message.chat.id, f"Ваше число: {my_bil}")
    
    if my_bil == vin_bil: 
        bot.send_message(message.chat.id, "Вы выиграли!")
    else:
        bot.send_message(message.chat.id, "Вы проиграли!")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'coin':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"Выбираем рандомную монету... Вам выпал(а): {money}")
    
    elif call.data == 'smile':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"Выбираем рандомный смайлик... Вам выпал: {smile}")

# Обработчик киков (в Телеграме это не так просто, как в Discord)
@bot.message_handler(commands=['kick09'])
def kick09(message):
    if message.reply_to_message:
        member_id = message.reply_to_message.from_user.id
        reason = message.text.split(' ', 1)[1] if len(message.text.split()) > 1 else "Без причины"
        
        # Здесь вам нужно будет реализовать логику удаления пользователя из группы
        # Например, если у вас есть администраторские права, вы можете удалить пользователя
        # бот.kick_chat_member(chat_id=message.chat.id, user_id=member_id)
        
        bot.send_message(message.chat.id, f'Пользователь {message.reply_to_message.from_user.username} был кикнут nПричина: {reason}')
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, ответьте на сообщение пользователя для кика.')

bot.polling(none_stop=True)
