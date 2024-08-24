#import path
from django.urls import path
from . views import TaskList,TaskDetail,TaskCreat,TaskUpdate,TaskDelete,UserLogin,UserLogout,RegistrationForm
urlpatterns=[
    path('login/',UserLogin.as_view(),name="login"),
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('task-create/',TaskCreat.as_view(),name="task-create"),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name="task-update"),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
    path('logout/',UserLogout.as_view(),name='logout'),
    path('signup',RegistrationForm.as_view(),name='signup'),


]