from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .forms import CustomUserCreationForm
from .models import CustomUser
# Create your views here.

def home(request):

    return render(request,'home.html')

class UserRegisterView(CreateView):
    model=CustomUser
    form_class=CustomUserCreationForm
    template_name='register.html'
    success_url=reverse_lazy('home')
