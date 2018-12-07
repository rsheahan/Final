from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Board, Picture
from .forms import localUsersForm, PictureForm


# Index -> Login View/Register/ViewBoard


def index(request):
    template = 'index.html'

    boards = Board.objects.all()

    context = {'boards': boards}


    return render(request, template, context)


def userIndex(request):
    if not request.user.is_authenticated:
        return redirect('loginView')

    template = 'userIndex.html'

    boards = Board.objects.all()

    context = {'boards': boards}

    currentUser = request.user

    print(currentUser)

    return render(request, template, context)


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


# Register

def register(request):
    if request.method == 'POST':

        form = localUsersForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            newUser = User(username=username, firstName=firstName, lastName=lastName, email=email,
                                 password=password)
            newUser.save()

            return redirect('loginView')

    else:

        form = localUsersForm()

    return render(request, 'register.html', {'form': form})


# User Index -> Profile/ Logout/ View Board/ Submit Picture

# Profile -> Edit Profile


def profileView(request):
    localUser = request.user

    template = 'profile.html'

    context = {'localUser': localUser}

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


def viewBoard(request, id):

    board = Board.objects.get(id=id)
    print(board)

    template = 'board.html'

    pictures = Picture.objects.all().filter(board=board)

    context = {'pictures': pictures}

    return render(request, template, context)


# View Picture -> Edit Picture


def viewPicture(request, id):
    template = 'picture.html'

    picture = Picture.objects.get(id=id)

    context={'picture':picture}

    print(picture.pic)

    return render(request, template, context)


# EditPicture -> Delete Picture


def editPicture(request):
    return redirect('viewPicture')


# Delete Picture


def deletePicture(request):
    return redirect('userIndex')


# Submit Picture


def submitPicture(request):
    if request.method == 'POST':

        form = PictureForm(request.POST)

        if form.is_valid():
            pic = form.cleaned_data['pic']
            picName = form.cleaned_data['picName']
            picDescription = form.cleaned_data['picDescription']
            board = form.cleaned_data['board']

            user = request.localUser

            owner = user.username

            print(owner)

            newPic = PictureForm(pic=pic, picName=picName, picDescription=picDescription, owner=owner,
                                 board=board)
            print(newPic.pic)

            newPic.save()

            return redirect('loginView')

    else:

        form = PictureForm()

    return render(request, 'submitPicture.html', {'form': form})



