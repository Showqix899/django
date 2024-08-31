from django.urls import path
from .views import HomeView,BlagPostForm,UserRegistration,UserLogin,UserLogOut,UserProfile,PostDelete,PostUpdate

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('create_post/',BlagPostForm.as_view(),name="create_post"),
    path('signup/',UserRegistration.as_view(),name="signup"),
    path('login/',UserLogin.as_view(),name="login"),
    path('logout/',UserLogOut.as_view(),name='logout'),
    path('profile/<str:username>',UserProfile.as_view(),name='profile'),
    path('delete/<int:pk>/',PostDelete.as_view(),name="delete"),
    path('update/<int:pk>/',PostUpdate.as_view(),name="update")
    

]
