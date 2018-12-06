from django import forms
from django.forms import ModelForm
from .models import localUsers, Picture


class localUsersForm(forms.Form):
    username = forms.CharField(required=True, max_length=60)
    firstName = forms.CharField(required=True, max_length=60)
    lastName = forms.CharField(required=True, max_length=60)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, max_length=60)


class PictureForm(forms.Form):
    pic = forms.ImageField(required=True)
    picName = forms.CharField(required=True, max_length=60)
    picDescription = forms.CharField(required=True, max_length=200)
    picDate = forms.DateTimeField(required=True)


class localUserForm(ModelForm):
    class Meta:
        model = localUsers
        fields = ['username', 'firstName', 'lastName', 'email', 'password']


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['pic', 'picName', 'picDescription', 'picDate']
