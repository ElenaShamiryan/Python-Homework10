from telebot import TeleBot
import telebot
from telebot import types
from datetime import datetime

bot = TeleBot('5738590398:AAGA88aPNQFrKizVTZuTZPOOYAGiA1O7rdo')


def my_log(msg: telebot.types.Message):
    with open('textfile.log', 'a', encoding='UTF-8') as n_log:
        print(datetime.today(), f'Пользователь ({msg.from_user.id}) ввел: {msg.text}', file=n_log)

def res_log(res):
    with open('textfile.log', 'a', encoding="utf-8") as n_log:
        print(datetime.today(), f'Калькулятор выдал результат {res}', file=n_log)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    with open('textfile.log', 'a', encoding='UTF-8') as n_log:
        print(datetime.today(), 'Начало работы', file=n_log)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/рациональные")
    btn2 = types.KeyboardButton("/комплексные")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я калькулятор!"
                                           "Пожалуйста, выберите числа, с которыми будете работать".format(message.from_user), reply_markup=markup) 

@bot.message_handler(commands=["рациональные"])
def handle_text(msg: telebot.types.Message):
        my_log(msg)
        bot.send_message(msg.chat.id, text="Введите 2 числа и действие между ними")
        bot.register_next_step_handler(callback=viev_rac_num, message=msg)

def viev_rac_num(msg: telebot.types.Message):
        my_log(msg)
        bot.send_message(chat_id=msg.from_user.id, text=rac_num(msg.text))

def rac_num(text):
    try:
        res = 0
        if "+" in text:
            lst = text.split('+')
            res = float(lst[0])+float(lst[1])
            res_log(res)
            return res
        elif "-" in text:
            lst = text.split('-')
            res = float(lst[0])-float(lst[1])
            res_log(res)
            return res
        elif "*" in text:
            lst = text.split('*')
            res = float(lst[0])*float(lst[1])
            res_log(res)
            return res
        elif "/" in text:
            lst = text.split('/')
            res = float(lst[0])/float(lst[1])
            res_log(res)
            return res            
        else:
            res = 'Введите /start, чтобы начать работу'
            res_log(res)
            return res          
    except:
        res = 'Я не понимаю запятых, поменяйте пожалуйста  на точки, и могу решать одно действие'
        res_log(res)
        return res


@bot.message_handler(commands=["комплексные"])
def handle_text(msg: telebot.types.Message):
        my_log(msg)
        bot.send_message(msg.chat.id, text="Введите 2 комплексных числа,"
                                           " например: 10+8j + 2-2j (с пробелом между ними)")
        bot.register_next_step_handler(callback=viev_rac_num2, message=msg)

def viev_rac_num2(msg: telebot.types.Message):
    my_log(msg)
    bot.send_message(chat_id=msg.from_user.id,  text=complex_num(msg.text))

def complex_num(text):
    res = None
    lst = text.split()
    if lst[1] == '-':
        res = complex(lst[0]) - complex(lst[2])
        res_log(res)
        return str(res)
    elif lst[1] == '+':
        res = complex(lst[0]) + complex(lst[2])
        res_log(res)
        return str(res)
    elif lst[1] == '/':
        res = complex(lst[0]) / complex(lst[2])
        res_log(res)
        return str(res)
    elif lst[1] == '*':
        res = complex(lst[0]) * complex(lst[2])
        res_log(res)
        return str(res)
    else:
        print('Неверный ввод')
@bot.message_handler()
def echo(msg: telebot.types.Message): 
    my_log(msg)
    bot.send_message(msg.from_user.id, "Введите /start, чтобы начать работу")


bot.polling(none_stop=True)
