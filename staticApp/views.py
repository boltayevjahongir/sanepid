from django.shortcuts import render

# Create your views here.
from newsApp.models import News


def home(request):
    news = News.objects.all()
    return render(request, 'home.html', context={
        'news':news
    })





def staticMenu(request, id):
    print(id)
    return render(request, 'static-menu.html')