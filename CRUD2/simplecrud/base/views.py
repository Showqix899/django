from django.shortcuts import render,redirect
from .models import Department,student
from .form import StudentForm

# Create your views here.
def home(request):
    students=student.objects.all()
    context={'students': students}
    return render(request, 'home.html',context)
def info(request,pk):
    i=int(pk)
    
    students=student.objects.get(id=i)
    context={'students': students}
    return render(request, 'info.html',context)
def add(request):
    forms=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
    context={'forms':forms}
    return render(request,'form.html',context)

