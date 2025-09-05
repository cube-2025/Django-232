from django.http import (HttpResponse, HttpResponseRedirect,
                         HttpResponsePermanentRedirect)
from django.shortcuts import render, redirect

def index(request):
    # return render(request, 'index.html')
    # data = {"header": "Параметр header",
    #         "message": "сообщение"}
    # return render(request, 'index_app1.html'
    #               ,context=data)
    # header = "Персональные данные"
    # langs = ["Русский", "Татарский", "Английский"]
    # user = {"name": "Никита", "age": 21}
    # addr = ("Мира", 10, 232)
    # data = {"header": header, "langs": langs, "user":user,
    #         "address": addr}
    # return render(request, 'index_app2.html',
    #               data)
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def contact(request):
    return redirect('about')

def details(request):
    return HttpResponsePermanentRedirect('/')