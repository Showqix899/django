from django.shortcuts import render
from django.http import HttpResponse
from .models import students,Dept,courses,biodata
# Create your views here.

# courses=[
#     {'id': 1,'name': 'Python'},
#     {'id': 2,'name': 'Java'},
#     {'id': 3,'name': 'C'},
#     {'id': 4,'name': 'C++'},
#     {'id': 5,'name': 'C#'},
# ]

def home(request):
    student=students.objects.all()
    context={'student':student}
    
    return render(request, 'base/home.html',context)
def info(request,pk):
    i=int(pk)
    if i:
        intel=students.objects.get(id=i)
        intelb=biodata.objects.get(id=i)
    else:
        pass
    context={'intel':intel,
             'intelb':intelb,
             }
    return render(request, 'base/info.html',context)