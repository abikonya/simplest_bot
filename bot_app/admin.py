from django.contrib import admin
from bot_app.models import BotUsers
from django.contrib.auth.models import Group


class BotUsersAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'name', 'surname', 'age')
    search_fields = ('telegram_id', 'name', 'surname', 'age')


admin.site.register(BotUsers, BotUsersAdmin)
admin.site.unregister(Group)
