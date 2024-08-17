from django.shortcuts import render
from django.shortcuts import  redirect
from .forms import userRegistration,recipeForm
from django.contrib.auth import authenticate,login,logout
from .models import recipe
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def home(request):
    querry=request.GET.get('q')
    if querry:
        recipes=recipe.objects.filter(
            Q(user__username__icontains=querry)|
            Q(name__icontains=querry)|
            Q(description__icontains=querry)|
            Q(ingrediant__icontains=querry)|
            Q(catagory__icontains=querry)
        ).order_by('-created_at')
    else:
        recipes=recipe.objects.all().order_by('-created_at')
    return render(request, 'home.html',{'recipes':recipes})


def register(request):
    msg=None
    if request.method == 'POST':
        form = userRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            msg="something went wrong. please try again !"

    else:
        form=userRegistration()
    return render(request,"signup.html",{'form':form,'msg':msg})


def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            msg="invalide username or password"
            return render(request,"login.html",{'msg':msg})
    
    return render(request,'login.html')
def userlogout(request):
    logout(request)
    return redirect('home')

def recipeAdd(request):
    if request.method=='POST':
        form=recipeForm(request.POST,request.FILES)
        if form.is_valid():
            recipe=form.save(commit=False)
            recipe.user=request.user
            recipe.save()
            return redirect('home')
        
    else:
        form=recipeForm()

    return render(request,'recipe_form.html',{'form':form})

def recipeEdit(request,pk):
    item=get_object_or_404(recipe,pk=pk,user=request.user)
    if request.method=='POST':
        form=recipeForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
           item = form.save(commit=False)
           item.user = request.user
           item.save()
           return redirect('home')
    else:
        form = recipeForm(instance=item)
    return render(request,'recipe_form.html',{'form':form})


def recipeDelete(request,id):
    item=get_object_or_404(recipe,id=id,user=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request,'confirmDelete.html',{"item":item})


def recipeInfo(requset,pk):
    item=recipe.objects.get(pk=pk)
    return render(requset,'recipe_info.html',{'item':item})

def userInfo(request,username):
    user=get_object_or_404(User,username=username)
    userPost=recipe.objects.filter(user=user).order_by('-created_at')
    return render(request,'user_info.html',{'userPost':userPost,'user':user})
@login_required
def likedRecipes(request,id):
    item=get_object_or_404(recipe,id=id)
    if not item.like.filter(id=request.user.id).exists():
        item.like.add(request.user)
    else:
        item.like.remove(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        
    
    







    

