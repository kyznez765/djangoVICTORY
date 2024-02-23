from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def index(req):
    items = Tovar.objects.all()
    data = {'tovari': items}
    return render(req, 'index.html', data)


def toCart(req):
    items = Cart.objects.all()
    total = 0
    for i in items:
        total += i.calcSumma()
    total = round(total, 2)
    data = {'tovari': items, 'total': total}
    return render(req,'cart.html', data)


def buy(req,id):
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


def delete(req,id):
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