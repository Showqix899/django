from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.UserRegisterView.as_view(),name="register"),
]
