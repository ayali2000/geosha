from dataclasses import fields
import profile
from pyexpat import model
from socket import fromshare
from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "rows":1
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "rows":1
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "rows":1
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"Confirm password",
        "rows":1
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "rows":1
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "rows":1
    }))


    model = User
    fields = ["username","email","first_name","last_name","password1","password2"]