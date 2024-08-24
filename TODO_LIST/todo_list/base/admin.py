from django.contrib import admin
#import Task from models
from .models import Task

# Register your models here.
admin.site.register(Task)