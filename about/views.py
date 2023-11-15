# about/views.py
from django.shortcuts import render
from .models import AboutMe

def about_me(request):
    about_info = AboutMe.objects.first()  # Assuming you only have one record in the AboutMe table
    return render(request, 'about/about_me.html', {'about_info': about_info})
