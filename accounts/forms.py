from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class Signup(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SignupUser(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'phoneNumber']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'phoneNumber']
        