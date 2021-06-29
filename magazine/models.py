from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(models.Model):
    password = models.CharField('Пароль', max_length=23)
    mail = models.CharField('Почта')

    def __str__(self):
        return self.password

    class Meta:
        verbose_name = 'Пароль'
        verbose_name_plural = 'Пароли'
