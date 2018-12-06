from django import forms
from django.forms import ModelForm
from .models import User, Picture


class UserForm(forms.Form):
    username = forms.CharField(required=True, max_length=60)
    firstName = forms.CharField(required=True, max_length=60)
    lastName = forms.CharField(required=True, max_length=60)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, max_length=60)


class PictureForm(forms.Form):
    pic = forms.ImageField(required=True)
    pic_name = forms.CharField(required=True, max_length=60)
    pic_description = forms.CharField(required=True, max_length=200)
    pic_date = forms.DateTimeField(required=True)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'firstName', 'lastName', 'email', 'password']


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['pic', 'pic_name', 'pic_description', 'pic_date']
