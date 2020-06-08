from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('book', views.book),
    path('Contact', views.contact),
    path('about', views.about),
    path('login', views.login),
    path('Home', views.home),
    path('register', views.register),
    path('Dashboard', views.dashboard),
    path('Mybookings', views.mybookings),
    path('Bustickets', views.bustickets),
    path('Buses', views.buses),
    path('Details', views.details)

]
