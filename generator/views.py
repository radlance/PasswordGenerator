from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('numbers'):
        characters.extend('0123456789')

    if request.GET.get('special'):
        characters.extend('!@#$^&%*()')

    try:
        length = int(request.GET.get('length', 12))
    except BaseException:
        return home(request)
    thepassword = ''
    for i in range(length):
        if len(thepassword) > 50:
            return render(request, 'generator/password.html', {'password': thepassword})
        thepassword += random.choice(characters)
    if thepassword is '':
        thepassword += '-'
    return render(request, 'generator/password.html', {'password': thepassword})
