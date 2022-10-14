from django.shortcuts import render

# Create your views here.

#
from newsApp.models import News
from staticApp.models import Menutext


def newsDetails(request, id):
    menu = Menutext.objects.all()
    news = News.objects.get(id=id)
    return render(request, 'news-detail.html',  context={
        'menu': menu,
        'news': news
    })

