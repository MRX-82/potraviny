from django import forms
from .models import User

class UserForm(forms.Form):
    name = forms.CharField(max_length=12)
    login = forms.CharField(max_length=16)
    number = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(max_length=20)

class EnterShop(forms.Form):
    login = forms.CharField(max_length=16)
    password = forms.CharField(max_length=20)