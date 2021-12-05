from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from features.models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ['username', 'email', 'password1', 'password2', 'professional', 'on_demand']


