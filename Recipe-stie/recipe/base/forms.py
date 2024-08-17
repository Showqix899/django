#import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import recipe

class userRegistration(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class recipeForm(forms.ModelForm):
    class Meta:
        model=recipe
        fields=['name','catagory','images','description','ingrediant']
