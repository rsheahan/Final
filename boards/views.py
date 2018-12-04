
from django.shortcuts import render, redirect
from boards.models import User


def index(request):

    template = 'index.html'

    return render(request, template)

#Index -> Login/ViewBoard/Register

def viewBoard(request):

    template = 'board.html'

    return render(request, template)

def login(request):

    if not request.user.is_authenticated:
        return render(request, 'register.html')

    return render(request, 'login.html')



#Login -> Register/Authenticate

#Register

def register(request):

    return render(request, 'register.html')

#If (new user) then add user else authenticate

def addUser(request):

    if request.method == 'POST':

        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        age = request.POST.get("age")
        email = request.POST.get("email")


        user = User(first_name = firstName, last_name = lastName, age = age, email = email)
        user.save()

        return redirect('index')


#Authenticate

def authenticate(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)

    if user is not None:
        login(request, user)
        return redirect('index')

    else:
        return render(request, 'login.html')


#View Board -> ViewPicture