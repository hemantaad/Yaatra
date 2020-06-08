import public as public
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date

from Registration.models import Buses, Driver


def about(request):
    return render(request, 'Registration/About.html')


def contact(request):
    return render(request, 'Registration/Contact.html')


def book(request):
    return render(request, 'Registration/Booking.html')


def home(request):
    return render(request, 'Registration/Home.html')


def dashboard(request):
    return render(request, 'Login/Dashboard.html')


def mybookings(request):
    return render(request, 'Login/Mybookings.html')


def bustickets(request):
    srs = Buses.objects.all()
    return render(request, 'Login/Bustickets.html', {'srs': srs})


def details(request):
    drv = Driver.objects.all()
    for s in drv:
        return render(request, 'Login/Details.html', {'drv': drv})


def buses(request):
    if request.method == "POST":
        source1 = str(request.POST['source'])
        destination1 = str(request.POST['destination'])
        date1 = request.POST['date']
        obj = Buses.objects.filter(source=source1, destination=destination1, date=date1)
        for s in obj:
             return render(request, 'Login/Buses.html', {'obj': obj})


    else:
        return render('Login/Buses.html', request)


def login(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password']
        x = auth.authenticate(username=username1, password=password1)
        if x is None:
            a = str('Invalid Username or Password!')
            return render(request, 'Registration/login.html', {'a': a})

        else:
            return redirect('/Dashboard')
    else:
        return render(request, 'Registration/login.html')


def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        x = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username,
                                     password=password)
        x.save()
        print('User Created')
        return redirect('/login')

    else:
        return render(request, 'Registration/register.html')
