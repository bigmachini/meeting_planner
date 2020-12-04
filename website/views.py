from datetime import datetime

from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")


def date(request):
    return HttpResponse(f'This page was served at {str(datetime.now())}')


def about(request):
    about = ' This is some important infomration about myself, \nI like to mountaineer \nI am in control of the mountains \nCheck this all out'
    return HttpResponse(about)
