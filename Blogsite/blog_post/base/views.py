from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.views.generic import ListView,DetailView
from .models import BlogPost
from django.views.generic import FormView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .forms import UserRegisterForm
#import login
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from .forms import UserLoginForm
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


# Create your views here.'

class UserRegistration(FormView):
    form_class=UserRegisterForm
    fields='__all__'
    template_name="userRegister.html"
    success_url=reverse_lazy('home')
    redirect_authenticated_user = True 
    def form_valid(self,form):
        user=form.save()
        if user is not None:
           login(self.request,user)
        return super(UserRegistration,self).form_valid(form)
    

class UserLogin(LoginView):
    form_class=UserLoginForm
    template_name="userLogin.html"
    success_url=reverse_lazy('home')
    # redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogOut(LogoutView):
    next_page=reverse_lazy('login')
    def dispatch(self,request):
        if request.user.is_authenticated:
            logout(request)
            return redirect(self.next_page)


   


class HomeView(ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name='posts' 

    def get_queryset(self):
        q=self.request.GET.get('q','')
        if q:
            return BlogPost.objects.filter(
                Q(subject__icontains= q)|
                Q(title__icontains=q)|
                Q(content__icontains=q)|
                Q(user__username__icontains=q)|
                Q(subject__icontains=q)
            )
        return super().get_queryset()


class BlagPostForm(LoginRequiredMixin,CreateView):
    model=BlogPost
    fields=['title','photo','subject','content']
    template_name="blog_form.html"
    success_url=reverse_lazy('home')
    login_url=reverse_lazy('login')


    def form_valid(self,form):
        form.instance.user=self.request.user
        form.save()
        success_msg="Your Articale has been Posted"
        return super(BlagPostForm,self).form_valid(form)
    
class UserProfile(LoginRequiredMixin,ListView):
    model=BlogPost
    template_name="userProfile.html"
    context_object_name='posts'
    login_url=reverse_lazy('login')

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs['username'])
        post=BlogPost.objects.filter(user=user)
        return post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_p'] = self.kwargs['username']
        return context
    
    login_url=reverse_lazy('login')


class PostDelete(LoginRequiredMixin,DeleteView):
    model=BlogPost
    template_name="delete.html"
    success_url=reverse_lazy('home')

    login_url=reverse_lazy('login')



class PostUpdate(LoginRequiredMixin,UpdateView):
    model=BlogPost
    fields=['title','photo','subject','content']
    template_name="update.html"
    success_url=reverse_lazy('home')


    login_url=reverse_lazy('login')

    

    








    


