from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('info/<str:pk>',views.info,name='info'),
    path('add/',views.add,name='add')
]