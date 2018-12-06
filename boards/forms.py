from django import forms
from django.forms import ModelForm
from .models import User, Picture


class UserForm(forms.Form):
    username = forms.CharField(max_length=60)
    firstName = forms.CharField(max_length=60)
    lastName = forms.CharField(max_length=60)
    email = forms.EmailField
    password = forms.CharField(max_length=60)


class PictureForm(forms.Form):
    pic = forms.ImageField
    pic_name = forms.CharField(max_length=60)
    pic_description = forms.CharField(max_length=200)
    pic_date = forms.DateField