import os;
import telebot;
import array as arr

bot = telebot.TeleBot('token')

class Runer:
    def __init__(self,name):
        self.name = name
        self.type = None
Runers ={}
@bot.message_handler(commands=['start'])
def start_command(message):
    msg = bot.reply_to(message,"Здравствуйте,пожалуйста введите ФИО")
    bot.register_next_step_handler(msg,process_FIO)
def process_FIO(message):
    try:
        id=message.chat.id
        name= message.text
        runer=Runer(name)
        Runers[id]=runer
        msg = bot.reply_to(message,"Пожалуйста введите тип забега:\n1)Тип0\n2)Тип1\n3)Тип2\n4)Тип3\n5)Тип4")
        bot.register_next_step_handler(msg, process_type)
    except:
        bot.reply_to(message,"Что-то пошло не так")

def process_type(message):
    try:
        id=message.chat.id
        type= message.text
        if (not type.isdigit()) or type<"0" or type >"6":
            msg = bot.reply_to(message,"введите число от 1 до 5")
            bot.register_next_step_handler(msg, process_type)
            return
        runer=Runers[id]
        runer.type=type
        msg = bot.reply_to(message,"Спасибо, проверьте введёные данные:\n"+Runers[id].name +"\nТип "+Runers[id].type)

    except:
        bot.reply_to(message,"Что-то пошло не так")


@bot.message_handler(commands=['my_data'])
def data_command(message):
    id = message.chat.id
    bot.reply_to(message,""+Runers[id].name +"\nТип "+Runers[id].type)

@bot.message_handler(commands=['all_runers'])
def list_command(message):
    list = "Список всех участников:\n"
    for i in Runers:
        list = list + Runers[i].name + "     Тип:"+Runers[i].type+"\n"
    bot.reply_to(message, list)
bot.polling(none_stop=True, interval=0)

