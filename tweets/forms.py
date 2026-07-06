from django import forms
from .models import Tweets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class tweet_form(forms.ModelForm):
    class Meta:
         model= Tweets
         fields=['text','photo']
    

class UserRegistrationForm(UserCreationForm):
     email=forms.EmailField()
     class Meta:
          model=User
          fields=('username','email','password1','password2')
     
