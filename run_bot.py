import telebot
import random
from telebot import types


# Загружаем список интересных фактов и поговорок
with open('data/facts.txt', 'r', encoding='utf-8') as f:
    facts = f.read().split('\n')

with open('data/thinks.txt', 'r', encoding='utf-8') as f:
    thinks = f.read().split('\n')

# Создаём бота
bot = telebot.TeleBot('Ваш токен')

text = 'Нажми: \nФакт - для получения интересного факта\nПоговорка - для получения мудрой цитаты'

# Команда start
@bot.message_handler(commands=['start'])
def start(m, res=False):
    # Добавляем кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Факт')
    item2 = types.KeyboardButton('Поговорка')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, text, reply_markup=markup)


# Получение сообщения от пользователя
@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = None
    # Если пользователь нажал на кнопку Факт
    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
    # Если пользователь нажал на кнопку Поговорка
    elif message.text.strip() == 'Поговорка':
        answer = random.choice(thinks)
    # Отправляем ответ пользователю
    bot.send_message(message.chat.id, answer)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
