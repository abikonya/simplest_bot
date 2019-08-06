from django.db import models


class BotUsers(models.Model):
    telegram_id = models.IntegerField(verbose_name='Telegram ID')
    name = models.CharField(max_length=64, verbose_name='Имя')
    surname = models.CharField(max_length=64, null=True, blank=True, verbose_name='Фамилия')
    age = models.IntegerField(null=True, blank=True, verbose_name='Возраст')

    def __str__(self):
        return '[BotUser #{id}]: {name} {surname}'.format(id=self.id, name=self.name, surname=self.surname)

    class Meta:
        verbose_name = 'Пользователь Бота'
        verbose_name_plural = 'Пользователи Бота'
