# https://docs.djangoproject.com/en/4.2/topics/auth/default/

from typing import Any
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs= {
                                 'placeholder': 'Enter email',}))

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    
    def __init__(self,*args :Any, **kwargs: Any) :
        super(RegisterForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'User name'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Reneter password'

    def clean_email(self):
        email= self.cleaned_data["email"]
        if User.objects.filter(email = email).exists():
            raise ValidationError("User already exists")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(required=True,widget=forms.TextInput(
        attrs= {'placeholder' : "user name",'autofocus':True }
    ))
    password= forms.CharField(required=True,
                              widget=forms.PasswordInput(
                                  attrs= {'placeholder' : 'Password'}))
