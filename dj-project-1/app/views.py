from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import pytz
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    template_name = 'app/time.html'
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    obj = datetime.datetime.now()
    new_tz = pytz.timezone('America/New_York')
    diff_times = {
        'Текущее время РФ:': obj,
        'Текущее время Нью-Йорк:': datetime.datetime.now(new_tz)
    }
    context = {
        'diff_times': diff_times
    }
    return render(request, template_name, context)


def workdir_view(request):
    directory = 'C:/Users/Admin/PycharmProjects/pythonProject11'
    workdir = os.listdir(directory)
    template_name = 'app/workdir.html'
    # raise NotImplemented
    return render(request, template_name, {'files': workdir})


