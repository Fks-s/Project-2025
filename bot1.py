import telebot
import threading
from telebot import types
import time

t = time.time()
# начальные переменные\initial variables (
# инициализация бота\initialization bot
bot = telebot.TeleBot("7791813689:AAHpszWsR4YX6VT6VfwAYQhMNpac1e0jk7g")
# статистика пользователя\users statistics
money = 0
dohod = 0
danue = None
names = None
years = None
pol = None
user_us = None
ank = False
# картинки\image
img = open("D:\\py_project\\old project\\tgbots\gameee\\fks_bor.png", 'rb')
money_photo = open('D:\\py_project\\old project\\tgbots\gameee\\money.png', 'rb')
dohod_photo = open('D:\\py_project\\old project\\tgbots\gameee\\money.png', 'rb')
farm_img = open('D:\\py_project\\old project\\tgbots\gameee\\farm.png', 'rb')
biznesy_img = open('D:\\py_project\\old project\\tgbots\gameee\\biznesy.png', 'rb')
kofeyna_img = open('D:\\py_project\\old project\\tgbots\gameee\\kofeyna.jpg', 'rb')
ofice_img = open('D:\\py_project\\old project\\tgbots\gameee\\ofice.jpg', 'rb')
upgrade_img = open('D:\\py_project\\old project\\tgbots\gameee\\upgradde.png', 'rb')
# улучшения бизнеса\upgrade business
farm_obr = False
farm_kulture = False
kofe_obr = False
kofe_sort = False
ofice_obr = False
ofice_AI = False
farm_tf = False
kofe_tf = False
ofice_tf = False

summa_perevoda = 0


# )
def add_money():
    global dohod
    global money
    global user_us
    while True:
        time.sleep(60)
        plus_minus_money(user_us.rstrip('\n'), dohod)


@bot.message_handler(commands=['start'])
def start(message):  # начальный скрипт/start script
    global user_us
    global ank
    file = open(message.from_user.username + '.txt', 'r')
    ff = file.readlines()
    if len(ff) > 0:
        user_us = ff[4]
        ank = True
    else:
        file = open('D:\\py_project\\old project\\tgbots\gameee\\' + message.from_user.username + '.txt', 'wb')
        file = open('D:\\py_project\\old project\\tgbots\gameee\\' + message.from_user.username + '.txt', 'a+',
                    encoding='utf-8')
        file.close()
        kebord = types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, text='как тебя зовут?', reply_markup=kebord)
        bot.register_next_step_handler(message, name)
    if len(ff) > 0:
        ank = True
    file.close()
    img = open('D:\\py_project\\old project\\tgbots\gameee\\fks_bor.png', 'rb')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.InlineKeyboardButton(text='создатель', url='T.me/Fks_s')
    btn2 = types.KeyboardButton(text='анкета')
    btn3 = types.KeyboardButton(text='мои данные')
    btn4 = types.KeyboardButton(text='капитал')
    btn5 = types.KeyboardButton(text='доход')
    btn6 = types.KeyboardButton(text='бизнесы')
    btn7 = types.KeyboardButton(text='перевести деньги')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    markup.add(btn6)
    markup.add(btn7)
    bot.send_photo(message.from_user.id, img, caption="Привет! Это бот фкс'а в нём ты можешь нихуя!",
                   reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):  # обработка сообщения пользователя / analysis user's message
    global dohod_photo
    global money_photo
    global dohod
    global money
    global biznesy_img
    global summa_perevoda
    global ank
    if message.text == 'анкета':

        if ank == False:
            file = open('D:\\py_project\\old project\\tgbots\gameee\\' + message.from_user.username + '.txt', 'wb')
            file = open('D:\\py_project\\old project\\tgbots\gameee\\' + message.from_user.username + '.txt', 'a+',
                        encoding='utf-8')

            file.close()
            kebord = types.ReplyKeyboardRemove()
            bot.send_message(message.from_user.id, text='как тебя зовут?', reply_markup=kebord)
            bot.register_next_step_handler(message, name)

        else:
            bot.send_message(message.from_user.id, text='Вы уже прошли анкету!')
            start(message)

    elif message.text == 'мои данные':
        my_danue_saved(message)

    elif message.text == 'доход':
        bot.send_photo(message.from_user.id, dohod_photo, caption=f'ваш доход: {dohod}$/секунду!')
        dohod_photo = open('D:\\py_project\\old project\\tgbots\gameee\\money.png', 'rb')

    elif message.text == 'капитал':
        file = open('D:\\py_project\\old project\\tgbots\gameee\\' + message.from_user.username + '.txt', 'r',
                    encoding='utf-8')
        ff = file.readlines()
        money = ff[3]
        file.close()
        bot.send_photo(message.from_user.id, money_photo, caption=f'ваш капитал содержит {money} $!')
        money_photo = open('D:\\py_project\\old project\\tgbots\gameee\\money.png', 'rb')

    elif message.text == 'бизнесы':
        markup2 = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='ферма 1000$')
        btn2 = types.KeyboardButton(text='кофейня 1000$')
        btn3 = types.KeyboardButton(text='офис 1000$')
        markup2.add(btn1)
        markup2.add(btn2)
        markup2.add(btn3)
        bot.send_photo(message.from_user.id, biznesy_img, caption='выбери какой бизнес купишь', reply_markup=markup2)
        biznesy_img = open('D:\\py_project\\old project\\tgbots\gameee\\biznesy.png', 'rb')
        bot.register_next_step_handler(message, vubor_biznesa)

    elif message.text == 'перевести деньги':
        bot.send_message(message.from_user.id, caption='сколько ты хочешь перевести?')
        bot.register_next_step_handler(message, choice_people)


def name(message):
    global names

    bot.send_message(message.from_user.id, text='красивое имя!')
    names = message.text
    file = open(message.from_user.username + '.txt', 'w', encoding='utf-8')
    file.write('имя: ' + names + "\n")
    file.close()
    bot.send_message(message.from_user.id, text='сколько тебе лет?')
    bot.register_next_step_handler(message, old)


def old(message):
    global years

    years = message.text
    file = open(message.from_user.username + '.txt', 'a+', encoding='utf-8')
    file.write('возраст: ' + years + '\n')
    file.close()
    bot.send_message(message.from_user.id, text='какого ты пола?')
    bot.register_next_step_handler(message, poll)


def poll(message):
    global pol
    global money
    global user_us
    money += 1000
    pol = message.text
    file = open(message.from_user.username + '.txt', 'a+', encoding='utf-8')
    file.write('пол: ' + pol + '\n' + str(money) + '\n' + message.from_user.username + '\n')
    user_us = message.from_user.username
    file.close()
    bot.send_message(message.from_user.id, text='хорошо, твои данные будут показаны через 1 секунду!')
    time.sleep(1)
    my_danue_anketa(message)


def my_danue_anketa(message):
    global names
    global years
    global pol
    global money

    bot.send_message(message.from_user.id, text=f"имя: {names}, возраст: {years}, пол: {pol} баланс: {money}")
    start(message)


def my_danue_saved(message):
    global danue
    global names
    global years
    global pol

    file = open("D:\\py_project\\old project\\tgbots\gameee\\" + message.from_user.username + '.txt', 'r',
                encoding='utf-8')
    danue = file.read()
    file.close()
    bot.send_message(message.from_user.id, text=danue)
    start(message)


def vubor_biznesa(message):  # выбор бизнеса\choice business
    global money
    global dohod
    global pol
    global ofice_tf
    global kofe_tf
    global farm_tf

    file = open('D:\\py_project\\old project\\tgbots\gameee\\' + message.from_user.username + '.txt', 'r',
                encoding='utf-8')
    ff = file.readlines()
    file.close()
    money = int(ff[3])

    if message.text == 'ферма 1000$' and money >= 1000 and farm_tf == False:
        farm_tf = True
        ferma(message)

    elif message.text == 'кофейня 1000$' and money >= 1000 and kofe_tf == False:
        kofe_tf = True
        kofeynya(message)

    elif message.text == 'офис 1000$' and money >= 1000 and ofice_tf == False:
        ofice_tf = True
        ofice(message)

    else:
        bot.send_message(message.from_user.id, text='бизнес уже есть или неправильный ввод')
        start(message)


def ofice(message):  # покупка офиса и его улучшение \ buying ofice and upgrade him
    global money
    global pol
    global dohod
    plus_minus_money(message.from_user.username, -1000)
    dohod += 12
    if pol == 'девушка':
        markup3 = types.ReplyKeyboardMarkup()
        btn11 = types.KeyboardButton('улучшить')
        btn12 = types.KeyboardButton('назад')
        markup3.add(btn11, btn12)
        bot.send_photo(message.from_user.id, ofice_img, caption='ты купила офис IT!', reply_markup=markup3)

    else:
        markup3 = types.ReplyKeyboardMarkup()
        btn11 = types.KeyboardButton('улучшить')
        btn12 = types.KeyboardButton('назад')
        markup3.add(btn11, btn12)
        bot.send_photo(message.from_user.id, ofice_img, caption='ты купил офис IT!', reply_markup=markup3)
    bot.register_next_step_handler(message, upgrade_ofice)


def upgrade_ofice(message):
    if message.text == 'назад':
        start(message)

    if message.text == 'улучшить':
        markup4 = types.InlineKeyboardMarkup()
        btn21 = types.InlineKeyboardButton('новое оборудование')
        btn22 = types.InlineKeyboardButton('использование ИИ')
        markup4.add(btn21, btn22)
        bot.send_photo(message.from_user.id, upgrade_img,
                       caption='выбери улучшение! \n купить новое оборудование $2000 \n использование ИИ $1000',
                       reply_markup=markup4)
        bot.register_next_step_handler(message, choice_upofice)


def choice_upofice(message):  # выбор улучшения для офиса \ choice upgrade for ofice
    global money
    global ofice_AI
    global ofice_obr
    global dohod
    file = open(message.from_user.username + '.txt', 'r', encoding='utf-8')
    ff = file.readlines()
    money = int(ff[3])
    file.close()
    if message.text == 'новое оборудование' and money >= 2000 and ofice_obr == False:
        ofice_obr == True
        dohod += 24
        bot.send_message(message.from_user.id, text=f'ваш доход: {dohod}/м!')
        plus_minus_money(message.from_user.username, -2000)
        time.sleep(2)
        start(message)

    if message.text == 'использование ИИ' and money >= 1000 and ofice_AI == False:
        ofice_AI == False
        dohod += 12
        bot.send_message(message.from_user.id, text=f'ваш доход: {dohod}/м!')
        plus_minus_money(message.from_user.username, -1000)
        time.sleep(2)
        start(message)


def kofeynya(message):  # покупка и прокачка кофейни\buying and upgrade coffee shop
    global kofe_obr
    global kofe_sort
    global pol
    global money
    global dohod
    global kofeyna_img

    plus_minus_money(message.from_user.username, -1000)

    if pol == 'девушка':
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton('улучшить')
        btn12 = types.KeyboardButton('назад')
        markup3.add(btn11, btn12)
        bot.send_photo(message.from_user.id, kofeyna_img, caption='ты купила кофейню!', reply_markup=markup3)
        dohod += 12

        if message.text == 'назад':
            start(message)
    else:
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton('улучшить')
        btn12 = types.KeyboardButton('назад')
        markup3.add(btn11, btn12)
        bot.send_photo(message.from_user.id, kofeyna_img, caption='ты купил кофейню!', reply_markup=markup3)
        dohod += 12
    kofeyna_img = open('kofeyna.jpg', 'rb')
    bot.register_next_step_handler(message, upgrade_kofe)


def upgrade_kofe(message):
    global money
    global kofe_sort
    global kofe_obr
    if message.text == 'назад':
        start(message)

    if message.text == 'улучшить':
        markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn112 = types.KeyboardButton('купить новое оборудование')
        btn122 = types.KeyboardButton('купить новые сорты кофе')
        markup4.add(btn112, btn122)
        bot.send_photo(message.from_user.id, kofeyna_img,
                       caption='выбери улучшение! \n купить новое оборудование $1250 \n купить новые сорты кофе $750',
                       reply_markup=markup4)


def choice_upkofe(message):  # выбор улучшения для кофейни \ choice upgrade for coffe shop
    global money
    global dohod
    global kofe_sort
    global kofe_obr
    file = open(message.from_user.username + '.txt', 'r', encoding='utf-8')
    ff = file.readlines()
    money = int(ff[3])
    file.close()
    if message.text == 'купить новые сорты кофе' and money >= 750:
        kofe_sort == True
        dohod += 9
        bot.send_message(message.from_user.id, text=f'ваш доход: {dohod}/м!')
        plus_minus_money(message.from_user.username, -750)
        time.sleep(2)
        start(message)
    if message.text == 'купить новое оборудование' and money >= 1250:
        kofe_obr == True
        dohod += 15
        bot.send_message(message.from_user.id, text=f'ваш доход: {dohod}/м!')
        plus_minus_money(message.from_user.username, -1250)
        time.sleep(2)
        start(message)


def ferma(message):  # покупка и прокачка фермы\buying and upgrade farm
    global farm_obr
    global farm_kulture
    global pol
    global money
    global dohod
    plus_minus_money(message.from_user.username, -1000)
    if pol == 'девушка':
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton('улучшить')
        btn12 = types.KeyboardButton('назад')
        markup3.add(btn11, btn12)
        bot.send_photo(message.from_user.id, farm_img, caption='ты купила ферму!', reply_markup=markup3)
        dohod += 12

    else:
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton('улучшить')
        btn12 = types.KeyboardButton('назад')
        markup3.add(btn11, btn12)
        bot.send_photo(message.from_user.id, farm_img, caption='ты купил ферму! Баланс = ' + str(money),
                       reply_markup=markup3)
        dohod += 12
    bot.register_next_step_handler(message, upgrade_farm)


def upgrade_farm(message):
    global farm_obr
    global farm_kulture
    global pol
    global money
    global dohod
    if message.text == 'назад':
        start(message)

    elif message.text == 'улучшить':
        markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn112 = types.KeyboardButton('новое оборудование')
        btn113 = types.KeyboardButton('новые культуры')
        btn114 = types.KeyboardButton('назад')
        markup4.add(btn112, btn113, btn114)
        bot.send_photo(message.from_user.id, upgrade_img,
                       caption='список улучшений \n новые культуры 500$ \n новое оборудование 1500$',
                       reply_markup=markup4)
        bot.register_next_step_handler(message, choise_upfarm)


def choise_upfarm(message):  # выбор улучшения для фермы \ choice upgrade for farm
    global farm_kulture
    global farm_obr
    global dohod
    file = open(message.from_user.username + '.txt', 'r', encoding='utf-8')
    ff = file.readlines()
    money = int(ff[3])
    file.close()
    if message.text == 'новое оборудование' and farm_obr == False and money >= 1500:
        dohod += 18
        bot.send_message(message.from_user.id, text=f'ваш доход: {dohod}/м!')
        plus_minus_money(message.from_user.username, -1500)
        farm_obr == True
        time.sleep(3)
        start(message)

    elif farm_obr == True:
        bot.send_message(message.from_user.id, text='уже куплено!')
        time.sleep(3)
        start(message)

    if message.text == 'новые культуры' and farm_kulture == False and money >= 500:
        dohod += 6
        bot.send_message(message.from_user.id, text=f'ваш доход: {dohod}/м!')
        plus_minus_money(message.from_user.username, -500)
        farm_kulture = True
        time.sleep(3)
        start(message)

    elif farm_kulture == True:
        bot.send_message(message.from_user.id, text='уже куплено!')
        time.sleep(3)
        start(message)

    if message.text == 'назад':
        start(message)


def plus_minus_money(uss, intt):  # продажа или покупка \ buying or selling
    global money
    file = open(uss + '.txt', 'r', encoding='utf-8')
    ff = file.readlines()
    print(ff[3])
    print(ff)
    file.close()
    money = int(ff[3]) + int(intt)
    ff[3] = str(money) + '\n'
    print(money)
    file = open(uss + '.txt', 'w', encoding='utf-8')
    for i in range(len(ff)):
        file.writelines(ff[i])
    file.close()


def choice_people(message):
    global summa_perevoda
    summa_perevoda = int(message.text)
    bot.send_message(message.from_user.id, text='кому ты хочешь отправить деньги (без @, @fks_s -- fks_s)')
    bot.register_next_step_handler(message, send_money)


def send_money(message):
    global money
    global summa_perevoda
    file = open(message.from_user.username + '.txt', 'r', encoding='utf-8')
    ff = file.readlines()
    m = int(ff[3])
    m -= summa_perevoda
    ff[3] = str(m) + '\n'
    file2 = open(message.text + '.txt', 'r', encoding='utf-8')
    fff = file2.readlines()
    mm = int(fff[3]) + summa_perevoda
    fff[3] = str(mm) + '\n'
    file2 = open(message.text + '.txt', 'w', encoding='utf-8')
    file = open(message.from_user.username + '.txt', 'w', encoding='utf-8')
    for i in range(len(fff)):
        file2.writelines(fff[i])

    for w in range(len(ff)):
        file.writelines(ff[w])

    file.close()
    file2.close()
    start(message)


threading.Thread(target=add_money, daemon=True).start()

bot.polling(none_stop=True, interval=0)
