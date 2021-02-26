"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging, ephem # Импортирование модуля регистрации и модуля астрономических величин

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters # Импортируем модули отвечающие за ком-цию с Telegram, обработку сообщенийб обработку команд

from datetime import date, datetime # Импортируем модули времени, что бы определять дату и время

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', # журнал для записи отчета о работе бота
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {                              # настройки прокси для обхода блокировок telegram
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context): # функция которая приветствует пользователя
    print('Вызван /start')      # вызывается если пользователь вводит \start 
    update.message.reply_text() # - отвечает пользователю отправляя сообщение через telegram
    

def talk_to_me(update, context):    # функция которая отвечает пользователю эхом
    user_text = update.message.text 
    print(user_text)                
    update.message.reply_text(text) 


def ask_planet(update, context): # функция которая должна отвечать пользователю если он ввел название планеты
    user_text = update.message.text   # получаем от пользователя сообщение
    user_text = user_text.split(' ')  # делаем список из сообщения пользователя

    if user_text[0] == "\planet":  #Перебираем планеты
        date = datetime.datetime(now)  # обозначили что нужна сегодняшняя дата
        if user_text == 'Mars':     # если тест от пользователя приравнен к слову Mars
            mars = ephem.Mars(date)  # то в переменную mars кладется расположение планеты сегодня
            update.message.reply_text(ephem.constellation(mars)) # выводится сообщение пользователю о созвездии
        if user_text == 'Venus':
            venus = ephem.Venus(date)
            update.message.reply_text(ephem.constellation(venus))
        if user_text == 'Mercury':
            mercury = ephem.Mercury(date)
            update.message.reply_text(ephem.constellation(mercury))
        if user_text == 'Jupiter':
            jupiter = ephem.Jupiter(date)
            update.message.reply_text(ephem.constellation(jupiter))
        if user_text == 'Saturn':
            saturn = ephem.Saturn(date)
            update.message.reply_text(ephem.constellation(saturn))
        if user_text == 'Uranus':
            uranus = ephem.Uranus(date)
            update.message.reply_text(ephem.constellation(uranus))
        if user_text == 'Neptune':
            neptune = ephem.Neptune(date)
            update.message.reply_text(ephem.constellation(neptune))
        if user_text == 'Pluto':
            pluto = ephem.Pluto(date)
            update.message.reply_text(ephem.constellation(pluto))


def main():                            # функция которая отвечает за работу бота
    mybot = Updater("1651502970:AAGSevR0qEcJqPh523rv-10fxT-ayFS8mL0", request_kwargs=PROXY, use_context=True) # ключ, настройки прокси

    dp = mybot.dispatcher # функция подключения к telegram
    dp.add_handler(CommandHandler("start", greet_user)) #вызов функции
    dp.add_handler(CommandHandler("planet", ask_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) # бот реагирует только на текстовые сообщения

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":  # запуск бота
    main()
