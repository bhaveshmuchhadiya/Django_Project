from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('home', views.home, name="home"),
    path('login', views.login, name="login"),
    path('process', views.process, name="process"),
    path('logout', views.logout, name="logout"),
]