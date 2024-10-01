from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.product_list,name='home'),
   path('product/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
   path('cart/',views.view_cart,name='view_cart'),
   path('cart/increase/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
    
]