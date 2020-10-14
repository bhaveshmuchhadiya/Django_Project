from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('leave_apply', views.leave_apply, name="leave_apply"),
    path('leave_details', views.leave_details, name="leave_details"),
    # path('home', views.home, name="home"),
    path('login', views.login, name="login"),
    path('process', views.process, name="process"),
    path('logout', views.logout, name="logout"),
    path('change_pass', views.change_pass, name="change_pass"),
]