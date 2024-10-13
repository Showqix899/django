from home.views import index,person,login,PersonAPI,PeoplViewSet,RegisterAPI,LoginAPI
from django.urls import path,include
from rest_framework.routers import DefaultRouter



router =DefaultRouter()
router.register(r'people',PeoplViewSet,basename='people')
urlpatterns=router.urls


urlpatterns = [
    path('index/',index),
    path('person/',person),
    path('login/',login),
    path('axiox/',PersonAPI.as_view()),
    path('',include(router.urls)),
    path('register',RegisterAPI.as_view()),
    path('login_reg',LoginAPI.as_view())
]