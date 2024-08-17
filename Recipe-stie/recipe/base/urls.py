from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),  
    path('login/',views.userlogin,name="login"),
    path('logout/',views.userlogout,name="logout"),
    path('recipeForm/',views.recipeAdd,name="recipeForm"),
    path('recipeEdit<int:pk>/',views.recipeEdit,name="recipeEdit"),
    path('recipeInfo<int:pk>/',views.recipeInfo,name="recipeInfo"),
    path('userInfo/<str:username>/',views.userInfo,name="userInfo"),
    path('liked_recipes<int:id>/',views.likedRecipes,name="liked_recipes"),
    path('recipeDelete<int:id>/',views.recipeDelete,name="recipeDelete"),

]
