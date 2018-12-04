
from django.shortcuts import render, redirect
from boards.models import User

#Index -> ViewBoard/Login/Register

def index(request):

    template = 'index.html'

    return render(request, template)

#View Board -> View Picture

def viewBoard(request):

    template = 'board.html'

    return render(request, template)

#Login -> Authenticate

def login(request):

    template = 'login.html'

    return render(request, template)

#Register -> Add User

def register(request):

    return render(request, 'register.html')

#Add User

def addUser(request):

    if request.method == 'POST':

        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        age = request.POST.get("age")
        email = request.POST.get("email")


        user = User(first_name = firstName, last_name = lastName, age = age, email = email)
        user.save()

        return redirect('index')

#Authenticate -> Authenticate/Register/Index

def authenticate(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)

    if User is not None:
        login(request, User)
        return redirect('index')

    else:
        return render(request, 'login.html')


#View Board -> ViewPicture