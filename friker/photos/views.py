from django.http import HttpResponse
from django.shortcuts import render

from friker.settings import STATIC_URL


def home(request):
    accesos = [
        {'name': 'Home',
         'url': '/'},
        {'name': 'About',
         'url': '/about'},
        {'name': 'Login',
         'url': '/login'}
    ]
    print("STATIC_URL=> " +STATIC_URL)
    return render(request, 'photos/home/index.html', {'accesos': accesos})
#   return HttpResponse("Hola Mundo ...")


def login(request):
    return render(request, 'photos/login/index.html', {})


def about(request):
    return render(request, 'photos/about/index.html', {})


