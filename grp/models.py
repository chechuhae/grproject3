from profile import Profile

from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta
from .widgets import BootstrapDateTimePickerInput



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=u"Пользователь")
    user_name = models.CharField(max_length=15, blank=False, verbose_name=u"Имя", null=True)
    user_surname = models.CharField(max_length=15, blank=True, verbose_name=u"Фамилия", null=True)
    avatar = models.FileField(verbose_name=u"Аватар", null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name=u"О себе")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"Город")
    birth_date = models.DateField(null=True, blank=True, verbose_name=u"Дата рождения")



class Cicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"Пользователь")
    last_cicle_first_date = models.DateField(null=True, blank=True, verbose_name=u"Начало последнего цикла")
    last_cicle_last_date = models.DateField(null=True, blank=True, verbose_name=u"Окончание последнего цикла")
    def counter(self):
        return self.last_cicle_first_date + timedelta(days=28) - date.today()
    created = models.DateTimeField(auto_now_add=True)
















