from django import forms
from .models import Tweet
#import user creation form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    #meta class
    class Meta:
        model = Tweet
        fields = ['text','photo']


class UserRegistrationFrom(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2']


