from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import date
from django.http import HttpResponse
from .models import InfoAdminUser

def Index(request):
    today = date.today()
    day = today.strftime("%d/%m/%Y")
    return render(request, 'home/index.html', {'today':day, 'nav':'home'})

def AboutView(request):
    info = InfoAdminUser.objects.all()
    return render(request, 'home/about.html', {'info':info,'nav':'about'})

