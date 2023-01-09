from django.db import models
from django.shortcuts import redirect

class Users(models.Model):
    name = models.CharField('Имя', max_length=50)
    login = models.CharField('Логин', max_length=250)
    age = models.PositiveIntegerField('Возраст')
    email = models.EmailField('Email')
    password = models.CharField('Пароль', max_length=255)

    def __str__(self):
        return self.login

    def get_absolute_url(self):
        return ''