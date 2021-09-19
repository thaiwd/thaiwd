from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('about/', views.AboutView, name='about'),
]