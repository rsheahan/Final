from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Picture


class UserForm(forms.Form):
    username = forms.CharField(required=True, max_length=60)
    first_name = forms.CharField(required=True, max_length=60)
    last_name = forms.CharField(required=True, max_length=60)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, max_length=60)


class PictureForm(forms.Form):
    pic = forms.ImageField(required=True)
    picName = forms.CharField(required=True, max_length=60)
    picDescription = forms.CharField(required=True, max_length=200)
    board = forms.CharField(required=True)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['pic', 'picName', 'picDescription', 'board']
