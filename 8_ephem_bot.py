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
import logging, ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from datetime import date, datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = "Введите название планеты на английском"
    print(text)
    update.message.reply_text(text)
    

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

planets = {
    'Mercury': ephem.Mercury(),
    'Venus': ephem.Venus(),
    'Mars': ephem.Mars(),
    'Jupiter': ephem.Jupiter(),
    'Saturn': ephem.Saturn(),
    'Uranus': ephem.Uranus(),
    'Neptune': ephem.Neptune(),
    'Pluto': ephem.Pluto(),
    }
def ask_planet(answers_constellation):
    date = datetime.datetime.now()
    while True:
        if user_text in planets:
          planet_obj = planets[planet_name]
    #planet_name = 'Mars'
          planet_obj.compute(date)
          print(ephem.constellation(planet_obj))

def main():
    mybot = Updater("1651502970:AAGSevR0qEcJqPh523rv-10fxT-ayFS8mL0", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, ask_planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
