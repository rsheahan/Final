
from django.shortcuts import render, redirect
from boards.models import User


def index(request):

    template = 'index.html'

    return render(request, template)

def viewRegister(request):

    return render(request, 'register.html')


def addUser(request):

    if request.method == 'POST':

        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        age = request.POST.get("age")
        email = request.POST.get("email")


        user = User(first_name = firstName, last_name = lastName, age = age, email = email)
        user.save()

        return redirect('index')
