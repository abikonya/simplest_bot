from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from config import token

from bot_app.views import UpdateBot

urlpatterns = [
    url('{}/'.format(token), UpdateBot.as_view(), name='update'),
]