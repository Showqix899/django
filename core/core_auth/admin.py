from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from .models import CustomUser


class CustomUserAdmin(BaseUserAdmin):

    list_display=('email','first_name','last_name','is_staff','is_superuser')
    list_filter=('is_staff','is_superuser','is_active')
    search_fields=('email','first_name','last_name')

    ordering=('email',)
    filter_horizontal=()

    fieldsets=(
        (None,{'fields':('email','password')}),
        ('Personal info',{'fields':('first_name','last_name')}),
        ('Permissions',{'fields':('is_active','is_staff','is_superuser')}),
        ('Important dates',{'fields':('last_login','date_joined')}),    
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
admin.site.register(CustomUser,CustomUserAdmin)