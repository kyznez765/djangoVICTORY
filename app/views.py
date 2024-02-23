from django.shortcuts import render

# Create your views here.


def index(req):
    data = {}
    return render(req,'index.html', data)