from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Board, Picture
from .forms import UserForm, PictureForm


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
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('userIndex')

    else:
        return redirect('loginView')


# Register

def register(request):
    if request.method == 'POST':

        form = UserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            firstName = form.cleaned_data['first_name']
            lastName = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            newUser = User.objects.create_user(username=username, password=password, email=email, first_name=firstName, last_name=lastName)


            return redirect('loginView')

    else:

        form = UserForm()

    return render(request, 'register.html', {'form': form})


# User Index -> Profile/ Logout/ View Board/ Submit Picture

# Profile -> Edit Profile


def profileView(request):
    user = request.user

    template = 'profile.html'

    context = {'user': user}

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

    user = request.user
    picture = Picture.objects.get(id=id)

    if user == picture.owner:
        redirect('authPicture.html')

    template = 'picture.html'

    picture = Picture.objects.get(id=id)

    context={'picture':picture}

    print(picture.pic)

    return render(request, template, context)


# EditPicture -> Delete Picture


def editPicture(request, id):

    picture = Picture.objects.get(id=id)

    form = PictureForm(request.POST or None, instance=picture)

    if form.is_valid():
            pic = form.cleaned_data['pic']
            picName = form.cleaned_data['picName']
            picDescription = form.cleaned_data['picDescription']
            board = form.cleaned_data['board']

            user = request.localUser

            owner = user.username

            print(owner)

            pic = PictureForm(pic=pic, picName=picName, picDescription=picDescription, owner=owner,
                             board=board)
            print(pic.pic)

            pic.save()
            return redirect('viewPicture')



    return render(request, 'editPicture.html', {'form':form, 'picture':picture})


# Delete Picture


def deletePicture(request, id):

    picture = Picture.objects.get(id=id)

    picture.delete()

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

            user = request.user

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



