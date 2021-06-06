from django.urls import path, include
from mail.views import home

urlpatterns = [
    path('', home, name='home-view'),
]