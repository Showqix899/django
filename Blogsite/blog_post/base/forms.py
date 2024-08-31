from typing import Any
from django import forms
from django.contrib.auth.models import User
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate



class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
                "class":"form-control",
                "placeholder":"Username",
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                "class":"form-control",
                "placeholder":"Email",
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                "class":"form-control",
                "placeholder":"Password",
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                "class":"form-control",
                "placeholder":"Confirm Password",
            }
        )


# class UserLoginForm(forms.Form):
#     username=forms.CharField(max_length=233,widget=forms.TextInput(attrs={'class':'form-controll','placeholder':'Enter Your Username'}))
#     password=forms.CharField(max_length=233,widget=forms.PasswordInput(attrs={'class':'form-controll','placeholder':'Enter Your Password'}))

#     def clean(self):
#         username=self.cleaned_data.get('username')
#         password=self.cleaned_data.get('password')
        
#         if username and password:
#             user=authenticate(username=username,password=password)
#             if not user:
#                 raise forms.ValidationError('Invalid username or password')
#         return self.cleaned_data



# class UserLoginForm(forms.Form):
#     username = forms.CharField(
#         max_length=233,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Username'})
#     )
#     password = forms.CharField(
#         max_length=233,
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'})
#     )
#     def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop('request', None)  # Remove 'request' from kwargs if present
#         super().__init__(*args, **kwargs)  # Call the parent constructor

#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')

#         if username and password:
#             user = authenticate(username=username, password=password)
#             if not user:
#                 raise forms.ValidationError('Invalid username or password')
#         return self.cleaned_data
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=233,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Username'})
    )
    password = forms.CharField(
        max_length=233,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'})
    )





    