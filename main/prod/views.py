from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Главная страница')
# def about(request):
#     return HttpResponse('<h2>О сайте</h2>')
# def contact(request):
#     return HttpResponse('<h1>Контакты</h1>')

def product(request, productid):
    output = '<h2>Продукт  {0}</h2>'.format(productid)
    return HttpResponse(output)
def users(request, id, name):
    output = '<h2>Пользователь</h2><h3>id:''{0} Имя: {1} </h3>'.format(id,name)
    return HttpResponse(output)