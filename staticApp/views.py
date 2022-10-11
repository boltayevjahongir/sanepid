from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')





def staticMenu(request, id):
    print(id)
    return render(request, 'static-menu.html')