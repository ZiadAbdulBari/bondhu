from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import fields
from App_Login.models import UserProfile

class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class EditProfile(forms.ModelForm):
    class Meta:
        model= UserProfile
        exclude=('user',)

