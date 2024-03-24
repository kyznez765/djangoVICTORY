# import telebot
import requests
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout

def index(req):
    items = Tovar.objects.all()
    data = {'tovari': items}
    return render(req, 'index.html', data)


def toCart(req):
    items = Cart.objects.all()
    forma = OrderForm()
    total = 0
    for i in items:
        total += i.calcSumma()
    total = round(total, 2)
    if req.POST:
        forma = OrderForm(req.POST)
        k1 = req.POST.get('adres')
        k2 = req.POST.get('tel')
        k3 = req.POST.get('email')
        if forma.is_valid():
            print(k1, k2, k3)
            k1 = forma.cleaned_data.get('adres')
            k2 = forma.cleaned_data.get('tel')
            k3 = forma.cleaned_data.get('email')
            print(k1, k2, k3)
            myzakaz = ''
            for one in items:
                myzakaz += one.tovar.name + ' '
                myzakaz += 'количество ' + str(one.count) + ' '
                myzakaz += 'сумма ' + str(one.summa) + ' '
                myzakaz += 'скидка ' + str(one.tovar.discount) + ' '
            neworder = Order.objects.create(adres=k1, tel=k2, email=k3,
                                            total=total, myzakaz=myzakaz,
                                            user=req.user)
            items.delete()


            telegram(neworder)

            return render(req, 'sps.html')

    data = {'tovari': items, 'total': total, 'formaorder': forma}
    return render(req, 'cart.html', data)


def buy(req, id):
    item = Tovar.objects.get(id=id)
    curuser = req.user
    if Cart.objects.filter(tovar=item, user=curuser):
        getTovar = Cart.objects.get(tovar_id=id)
        getTovar.count += 1
        getTovar.summa = getTovar.calcSumma()
        getTovar.save()
    else:
        Cart.objects.create(tovar=item, count=1, user=curuser, summa=item.price)
        data = {}
    return redirect('home')


def delete(req, id):
    item = Cart.objects.get(id=id)
    item.delete()
    return redirect('tocart')


def cartCount(req, num, id):
    num = int(num)
    item = Cart.objects.get(id=id)
    item.count += num
    if item.count < 0:
        item.count = 0
    item.summa = item.calcSumma()
    item.save()
    return redirect('tocart')


def telegram(neworder):
    token = '7123230685:AAGioh4_I7QBRjK8IPpIOGbS5g0MwvkP9ew'
    chat = '528849379'
    message = neworder.user.username + ' , новый заказ ,' + neworder.tel + ' ,' + neworder.myzakaz + ' ,' + neworder.adres + ' ,' + neworder.email
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat}&text={message}"
    requests.get(url)


def reg(req):
    if req.POST:
        f = SignUp(req.POST)

        if f.is_valid():
            f.save()

            k1 = f.cleaned_data.get('username')
            k2 = f.cleaned_data.get('password1')
            k3 = f.cleaned_data.get('email')
            k4 = f.cleaned_data.get('first_name')
            k5 = f.cleaned_data.get('last_name')

            user = authenticate(username=k1, password=k2)
            newuser = User.objects.get(username=k1)

            newuser.email = k3
            newuser.first_name = k4
            newuser.last_name = k5
            newuser.save()

            ProfileUser.objects.create(user_id=newuser.id)

            login(req, newuser)
            return redirect('home')
    else:
        f = SignUp()
    data = {'forma': f}
    return render(req, 'registration/registration.html', data)



def logout(req):
    auth_logout(req)
    print(123)
    return redirect('home')
