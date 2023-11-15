# about/urls.py
from django.urls import path
from .views import about_me

urlpatterns = [
    path('about/', about_me, name='about_me'),
    path('josh/', about_me, name='about_me'),
    path('', about_me, name='about_me'),
]
