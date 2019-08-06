import telebot
import re

from rest_framework.response import Response
from rest_framework.views import APIView

import config

from bot_app.models import BotUsers

bot = telebot.TeleBot(config.token)


class UpdateBot(APIView):
    def post(self, request):
        json_string = request.body.decode("UTF-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])

        return Response({'code': 200})


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')
    bot.send_message(message.chat.id, 'Давай знакомиться! Как твое имя?')


@bot.message_handler(func=lambda message: re.search(r'^[а-яА-Яa-zA-Z]+\D+$', message.text))
def get_name_surname(message):
    try:
        update_user = BotUsers.objects.filter(telegram_id=message.chat.id).latest('id')
        if update_user.age is True:
            def new_user():
                new_user = BotUsers(telegram_id=message.chat.id, name=message.text)
                new_user.save()
                bot.send_message(message.chat.id, 'Приятно познакомиться, {}'.format(message.text))
                bot.send_message(message.chat.id, 'И фамилия у тебя тоже наверное есть?')
        else:
            update_user.surname = message.text
            update_user.save(update_fields=['surname'])
            bot.send_message(message.chat.id, '{name} {surname} - это звучит гордо!'.format(name=update_user.name,
                                                                                            surname=update_user.surname))
            bot.send_message(message.chat.id, 'А сколько лет тебе?')
    except:
        new_user()


@bot.message_handler(func=lambda message: re.search(r'^[0-9]+$', message.text))
def end(message):
    update_user = BotUsers.objects.last('id')
    update_user.age = message.text
    update_user.save(update_fields=['age'])
    bot.send_message(message.chat.id, 'Ну что ж, приятно познакомиться {name} {surname}. Рад что тебе {age}'.format(name=update_user.name,
                                                                                                                    surname=update_user.surname,
                                                                                                                    age=update_user.age))

