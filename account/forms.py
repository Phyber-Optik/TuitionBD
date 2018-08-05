from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    username = forms.CharField(max_length=30, required=True, help_text='Required For Log in')
    phone = forms.CharField(max_length=20, required=False, help_text='Optional')
    email = forms.EmailField(max_length=30, required=True, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'password1', 'password2')
