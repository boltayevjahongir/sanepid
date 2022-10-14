from django.urls import path
from .views import newsDetails

urlpatterns = [
    # path('', home, name='home'),
    path('news-detail/<int:id>', newsDetails, name='newsDetails')
]