import timeit
import os
from telethon.sync import TelegramClient
import time
import pyautogui as pg
import colorama
from colorama import Back, Fore, Style

API_ID = 7108918
API_HASH = "dece7611717647a28d7ac863c8224658"
TOKEN = '941547549:AAFuHp0mXWkFFBKT_rUzgPdKbLBhgWCR-q4'
from telethon import events

client = TelegramClient('+213792473466', API_ID, API_HASH)  # nomer 213790444304
client.start()  # запускаем клиент
bot = 'vktarget_bot'
dlgs = client.get_dialogs()  # получаем все наши названия каналов, групп в которых мы состоим
for dlg in dlgs:
    if dlg.title == 'vktarget':
        btc = dlg  # находим нужный диалог и записывем его данные в переменную


def get_t(s):  # функция для получения числа из строки
    l = len(s)
    integ = 10
    i = 0
    while i < l:
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            return int(s_int)


i = 0




print(Fore.YELLOW + 'ISh Boshlandi')


def send_msg_to_work():  # функция отправки сообщений к ботту для посещения сайтов
    global i
    client.send_message('vktarget', 'Задания')  # отправляем команду к боту
    i += 1
    time.sleep(1)  # ждем пока бот обработает наш запрос и отправит ссылку
    get_msg = client.get_messages(btc, limit=1)  # получаем сообщение которое нам отослал бот
   # print(get_msg[0].message)
    if get_msg[0].message == 'Начали поиск заданий..':
        print(Fore.RED + '🛌 dam olarkamam')
        time.sleep(60)
        print('damda 1min')
        client.send_message('vktarget', 'Задания')
        time.sleep(2)
        if get_msg[0].message == 'Начали поиск заданий..':
            print(Fore.YELLOW + '1yo\'q')
            client.send_message('vktarget', 'Задания')
            time.sleep(2 * 60)
            if get_msg[-1].message == 'Начали поиск заданий..':
                print(Fore.RED + '2😅 Baribir chiqmadi 😅')
                time.sleep(60)
                client.send_message('vktarget', 'Задания')
                time.sleep(2)
                if get_msg[-1].message == 'Начали поиск заданий..':
                    print('3Vazifa yo\'q dam_2min ')
                    time.sleep(50)
                    client.send_message('vktarget', 'Задания')
                else:
                    print(Fore.RESET + get_msg[-1].message)
            else:
                print('2chiqdi')
        else:
            print('1chiqdi!')
    else:
        print(Fore.GREEN + 'Vazifa bor davom etarkanman')
    if get_msg[-1].message == 'Начали поиск заданий..':
        print('Vazifa yo\'q dam_2min ')
        time.sleep(2 * 60)
    else:
        m1 = get_msg[0].click(-1)  # нажымаем кнопку с ссылкой в сообщении бота. По ней нас отправляет на сай

#
        if m1.message == 'Начали поиск заданий..':
            print('vazifa yo\'q ekan 💤️')
            time.sleep(50)
        elif m1.message == 'Начали поиск заданий..':
            print('yana vazifa yo\'q ekan 💤️')
            time.sleep(50)
        else:
            print(Fore.CYAN + '👨‍💻👨‍💻vazifa bajatmoqda👨‍💻👨‍💻')

        if m1.message == 'Ошибка при проверке':
            print(Fore.RED + '⛔ Eplolmadi ⛔')
            time.sleep(5)
            get_msg[0].click(-2)
            time.sleep(2)

        else:
            print(Fore.MAGENTA + '🤑 Bajardi 🤑')
        time.sleep(1)

    time.sleep(2)  # ждем  прогрузки всех елементов сайта
    # нажымаем не рекапчу, которая может быть на сайте. Возможна жоработка с машшыным зрением, но я решил не заморачивться и просто кликать на капчу и не проверять ее наличие на дынном сайте
    time.sleep(2)
    time_msg = client.get_messages(btc,
                                   limit=1)  # при переходе на сайт боот автоматически отправляет нам сообщение в котором написано сколько я должен бцде провести времени на сайте
    st = time_msg[-1].message  # переменая в которой содержиться текст последнего сообщения
#    print(st)


    s = st
    integ = 10  # количесво секунд для задержки скрипта
    if get_t(st) == None:  # проверяем если функция не нашла число в строке тогда ничего не делаем
        pass
    else:
        integ = get_t(st)  # если нашла то присваиваем переменой времени то число которае нам возвратила функция
    if integ > 60:
        integ = 20
    elif integ < 10:
        integ = 10

    print(Fore.BLUE + 'sleep - ' + str(integ))
    time.sleep(integ)  # задерживаем скрипт


while True:  # бесконечный цикл
    send_msg_to_work()
    print('Task number - ' + str(i))
    if str(i) == "15":
        print('💻 xarakat 15ta yetti 20min 🛌 dam olaman')
        time.sleep(60 * 20)
    elif str(i) == "25":
        print('💻 xarakat 25 ta yetti 40 min 🛌 dam olaman')
        time.sleep(60 * 40)