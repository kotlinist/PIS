from django.http import HttpResponse

from django.shortcuts import render
from django import template

def home(request):
    # return HttpResponse(u'Привет, Мир!', content_type="text/plain")
    # return HttpResponse(u'Привет, Мир!')
    return render(request, 'templates/index.html')

