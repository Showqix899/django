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
            return redirect('home')
    context={'forms':forms}
    return render(request,'form.html',context)
    

def update(request,pk):
    i=int(pk)
    info_tobeUpdate=student.objects.get(id=i)
    forms=StudentForm(instance=info_tobeUpdate)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=info_tobeUpdate)
        if form.is_valid:
            form.save()
            return redirect('home')
    return render(request,'form.html',{'forms':forms})

def delete(request,pk):
    form=student.objects.get(id=pk)
    if request.method=='POST':
        form.delete();
        return redirect('home')
    return render(request,'delete.html',{'form':form})

