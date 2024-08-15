from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
#import redirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    gender=[
       '','male','female','Custom'
    ]
    errors={}
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        gen=request.POST.get('gender')
        if pass1!=pass2:
            errors['pass2']='passwords do not match'
            confirmation=False
        if User.objects.filter(username=username).exists():
            errors['username']='this username is already taken, tyr another one..'
            confirmation=False
        if User.objects.filter(email=email).exists():
            errors['email']='Email already exists'
            confirmation=False
        if not username or not email or not pass1 or not pass2 or gen=='':
            errors['blank']='Please fill all the fields'
            confirmation=False
        if not errors:
            user=User.objects.create_user(username=username,email=email,password=pass1)
            user.gender=gen
            user.save()
            messages.success(request,'user created successfully')
            return redirect('signin')
        else:
            messages.error(request,"somethings went wrong")

    return render(request, 'signup.html',{'gender':gender,'errors':errors})



def signin(request):
    errorms=None
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('home')
        else:
            messages.error(request,"Invalid username or password")
        


    return render(request,'signin.html')



def home(request):
    return render(request,'home.html')


def signout(request):
    logout(request)
    return redirect('home')
