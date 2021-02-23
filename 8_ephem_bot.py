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
    update.message.reply_text('Введите название планеты на английском') # - отвечает пользователю отправляя сообщение через telegram
    

def talk_to_me(update, context):    # функция которая отвечает пользователю эхом
    user_text = update.message.text 
    print(user_text)                
    update.message.reply_text(text) 

planets = {                         # словарь с названием планет в ключе и с ссылками на созвездия в значении
    'Mercury': ephem.Mercury(),
    'Venus': ephem.Venus(),
    'Mars': ephem.Mars(),
    'Jupiter': ephem.Jupiter(),
    'Saturn': ephem.Saturn(),
    'Uranus': ephem.Uranus(),
    'Neptune': ephem.Neptune(),
    'Pluto': ephem.Pluto(),
    }
def ask_planet(update, context): # функция которая должна отвечать пользователю если он ввел название планеты
    user_text = update.message.text   # получаем от пользователя сообщение
    print(user_text)
    user_text = user_text.split(' ')
    print(user_text)
    date = datetime.datetime.now()     # создание переменной, которая ссылается на модуль datetime и обозначает время сейчас
    while True:                        # цикл, который должен запускаться если пол-тель ввел название планеты которая есть в словаре
        if user_text in planets.values:       # если текст пользователя есть в списки планет
          planet_obj = planets[planet_name] # ссылаемся на значение в словаре
          #planet_name = 'Mars'        
          planet_obj.compute(date)     # добавляем значению в словаре дату(сегодня)
          print(ephem.constellation(planet_obj)) # отвечаем пользователю

def main():                            # функция которая отвечает за работу бота
    mybot = Updater("1651502970:AAGSevR0qEcJqPh523rv-10fxT-ayFS8mL0", request_kwargs=PROXY, use_context=True) # ключ, настройки прокси

    dp = mybot.dispatcher # функция подключения к telegram
    dp.add_handler(CommandHandler("start", greet_user, ask_planet)) #вызов функции
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) # бот реагирует только на текстовые сообщения

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":  # запуск бота
    main()
