from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Index -> ViewBoard/Login/Register

def index(request):
    template = 'index.html'

    return render(request, template)


# View Board -> View Picture

def viewBoard(request):
    template = 'board.html'

    return render(request, template)


# Login -> Check User

def loginView(request):
    template = 'login.html'

    return render(request, template)


# Register -> Add User

def register(request):
    return render(request, 'register.html')


# Add User

def addUser(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username = username, first_name=firstName, last_name=lastName, email=email, password=password)
        user.save()

        return redirect('index')


# Check User -> Login/User Index

def checkUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return render(request, 'userindex.html')

    else:
        return render(request, 'login.html')

# View Board -> ViewPicture
