from django.urls import path
from .views import home, staticMenu

urlpatterns = [
    path('', home, name='home'),
    path('static-menu/<int:id>', staticMenu, name='staticMenu')
]