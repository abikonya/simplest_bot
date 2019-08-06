import telebot

from rest_framework.response import Response
from rest_framework.views import APIView

import config

bot = telebot.TeleBot(config.token)


class UpdateBot(APIView):
    def post(self, request):
        json_string = request.body.decode("UTF-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])

        return Response({'code': 200})


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Welcome')
