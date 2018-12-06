from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Board, User, Picture
from .forms import UserForm, PictureForm


# Index -> Login View/Register/ViewBoard


def index(request):
    template = 'index.html'

    return render(request, template)


def userIndex(request):
    if not request.user.is_authenticated:
        return redirect('loginView')

    template = 'userIndex.html'

    return render(request, template)


# Login View -> Check User


def loginView(request):
    template = 'login.html'

    return render(request, template)


# Check User -> User Index/ Login View (Failed Login Attempt)


def checkUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('userIndex')

    else:
        return redirect('loginView')


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

        newUser = User(username=username, first_name=firstName, last_name=lastName, email=email,
                       password=password)
        newUser.save()

        return redirect('index')


# User Index -> Profile/ Logout/ View Board/ Submit Picture

# Profile -> Edit Profile


def profileView(request):

    user = request.user

    template = 'profile.html'

    context = {'currentUser', user}

    return render(request, template, context)


# Edit Profile

def editProfile(request):
    # todo

    return redirect('profileView')


# Logout


def logoutView(request):
    logout(request)

    return redirect('index')


# View Board -> View Picture


def viewBoard(request):
    template = 'board.html'



    return render(request, template)


# View Picture -> Edit Picture


def viewPicture(request):
    template = 'picture.html'

    return render(request, template)


# EditPicture -> Delete Picture


def editPicture(request):
    return redirect('viewPicture')


# Delete Picture


def deletePicture(request):
    return redirect('userIndex')


# Submit Picture -> Add Picture


def submitPicture(request):
    return redirect('addPicture')


# Add Picture


def addPicture(request):
    return redirect('userIndex')
