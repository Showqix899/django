from django.contrib import admin
from .models import courses,students,Dept,biodata


# Register your models here.

admin.site.register(students)
admin.site.register(Dept)
admin.site.register(courses)
admin.site.register(biodata)



