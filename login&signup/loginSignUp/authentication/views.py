from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):

    return render(request,'authentication/index.html')
def signup(request):
    ms=""
    ms2=False
    if request.method=='POST':
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if User.objects.filter(username=username).exists():
            messages.error(request,"This user name is all ready taken, try another one")
            return redirect('home')
        if User.objects.filter(email=email).exists():
            messages.error(request,"This email is all ready taken, try another one")
            return redirect('home')
        if not fname or not lname or not pass1:
            messages.error(request,"Please fill all the fields")
            return redirect('home')
        if pass1==pass2:
            myuser=User.objects.create_user(username,email,pass1)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()

            subject="wellcome to lino!"
            message="hello "+myuser.first_name+" "+myuser.last_name+" \n"+"thanks for visiting our site. we have sent a confirmation email please activate your account..."
            from_email=settings.EMAIL_HOST_USER
            to_list=[myuser.email]
            send_mail(subject,message,from_email,to_list, fail_silently=True)
            #why it's not sending the email?



            return redirect('signin')
        else:
            ms="passwords is not matching"
            ms2=True


    return render(request,'authentication/signup.html',{'ms':ms,'ms2':ms2})

def signin(request):
    if request.method=='POST':
        username=request.POST.get('ue')
        password=request.POST.get('pass1')

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            fname=user.first_name
            lname=user.last_name
            return render(request,'authentication/index.html',{'fname':fname,'user':user})
        else:
            messages.error(request,"bad requrest")
            return redirect('home')
    
    return render(request,'authentication/signin.html')
def signout(request):
    logout(request)
    return redirect('home')
