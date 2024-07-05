from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('info/<str:pk>',views.info,name='info'),
    path('add/',views.add,name='add'),
    path('update/<str:pk>/',views.update,name='update-room'),
    path('delete/<str:pk>/',views.delete,name='delete-room'),


]