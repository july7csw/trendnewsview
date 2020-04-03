from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    lastlist = News.objects.last()
    lastperiod = lastlist.period
    recentlist = News.objects.filter(period=lastperiod)
    return render(request, 'siteapp/index.html', {"recentlist":recentlist})

def getrecentlist(request):
    recentlist = News.objects.all()
    return render(request, 'siteapp/main.html', {"recentlist":recentlist})