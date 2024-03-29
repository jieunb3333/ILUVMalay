from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class SignUpForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','email']

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())