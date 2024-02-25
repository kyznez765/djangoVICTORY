from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator


class OrderForm(forms.Form):
    adres = forms.CharField(label='Адрес доставки')
    tel = forms.CharField(label='Телефон', validators=[
        RegexValidator('^\\+7-\\d{3}-\\d{3}-\\d{2}-\\d{2}$', message='введите тел +7-***-***-**-**')])
    email = forms.EmailField(label='Эл. почта')


class SignUp(UserCreationForm):
    username = forms.CharField(label='логин',
                               help_text='',
                               widget=forms.TextInput(attrs={'placeholder': 'username'}
                                                      ))
    password1 = forms.CharField(label='пароль',
                                help_text='', widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password"}
        )
                                )
    password2 = forms.CharField(label='подтверждение',
                                help_text='', widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password"}
        )
                                )
    email = forms.EmailField(label='почта',
                             widget=forms.TextInput(attrs={'placeholder': 'qwe@mail.ru'})
                             )
    first_name = forms.CharField(label='имя', max_length=20, required=False)
    last_name = forms.CharField(label='фамилия', max_length=20, required=False)


