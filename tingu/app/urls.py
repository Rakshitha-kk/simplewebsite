
from django.urls import path
from app import views
urlpatterns = [
    path("",views.home,name="home"),
    path("login1",views.login1,name="login1"),
    path("login2",views.login2,name="login2"),
    path("reg",views.reg,name="reg"),
    path("reg1",views.reg1,name="reg1"),
]