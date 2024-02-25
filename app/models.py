from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Tovar(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название товара')
    price = models.IntegerField(verbose_name='Цена')
    image = models.CharField(max_length=1000, verbose_name='Картинка')
    discount = models.FloatField(default=0, verbose_name='Скидка')

    def __str__(self):
        return self.name


class Cart(models.Model):
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    count = models.IntegerField()
    summa = models.DecimalField(decimal_places=2, max_digits=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.tovar

    # подсчет суммы
    def calcSumma(self):
        return self.count * (self.tovar.price - self.tovar.discount / 100 * self.tovar.price)

    # табличка заказы


class Order(models.Model):
    adres = models.CharField(max_length=150)
    tel = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    total = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    myzakaz = models.TextField()


# ----------------------------------------------------------
class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # podpiska = models.ForeignKey(Podpiska, on_delete=models.SET_NULL, null=True)
    # balance = models.IntegerField(default=10)
