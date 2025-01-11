from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)  # Имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс
    age = models.IntegerField()  # Возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Название игры (уникальное)
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер файла
    description = models.TextField()  # Описание
    age_limited = models.BooleanField(default=False)  # Ограничение возраста 18+
    buyers = models.ManyToManyField(Buyer, related_name='games')  # Покупатели игры

    def __str__(self):
        return self.title
