from django import forms
from django.core.validators import RegexValidator

from .models import *


class OrderForm(forms.Form):
    adres = forms.CharField(label='Адрес доставки')
    tel = forms.CharField(label='Телефон', validators=[RegexValidator('^\\+7-\\d{3}-\\d{3}-\\d{2}-\\d{2}$', message='введите тел +7-***-***-**-**')])
    email = forms.EmailField(label='Эл. почта')