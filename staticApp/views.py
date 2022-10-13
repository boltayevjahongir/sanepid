from django.shortcuts import render

# Create your views here.
from newsApp.models import News
from staticApp.models import Menutext


def home(request):
    news = News.objects.all()
    menu = Menutext.objects.all()
    return render(request, 'home.html', context={
        'news': news,
        'menu': menu
    })


def staticMenu(request, id):
    menu = Menutext.objects.all()
    return render(request, 'static-menu.html',  context={
        'menu': menu
    })
