from django.shortcuts import render,redirect
#httpresponse
from django.http import HttpResponse
from django.views.generic.list import ListView
#DetailView
#import logout
#import authenticate
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import logout,login
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Task

from django.contrib.auth.mixins import LoginRequiredMixin

class RegistrationForm(FormView):
    form_class = UserCreationForm
    fields='__all__'
    template_name='base/register.html'
    success_url=reverse_lazy('tasks')
    redirect_authenticated_user=True

    def form_valid(self,form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegistrationForm,self).form_valid(form)

class UserLogin(LoginView):
    fields='__all__'
    template_name="base/login.html"
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
class UserLogout(LogoutView):
    next_page=reverse_lazy('login')
    def dispatch(self,request):
        if request.user.is_authenticated:
            logout(request)
            return redirect(self.next_page)
        else:
            return HttpResponse("something went wrong")


class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name='tasks'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks']=context['tasks'].filter(user=self.request.user)
        context['count']=context['tasks'].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name='detail'
    template_name='base/task.html'


class TaskCreat(LoginRequiredMixin,CreateView):
    model=Task
    fields=['title','description','complete']
    success_url=reverse_lazy('tasks')

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(TaskCreat,self).form_valid(form)


class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title','description','complete']
    success_url=reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name='task'
    template_name='base/delete.html'
    success_url=reverse_lazy('tasks')
