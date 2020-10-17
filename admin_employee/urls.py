from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/admin_index', views.index, name="index"),
    path('admin/add_department', views.add_department, name="add_department"),
    path('admin/view_department', views.view_department, name="view_department"),
    path('admin/add_leave', views.add_leave, name="add_leave"),
    path('admin/view_leave_type', views.view_leave_type, name="view_leave_type"),
    path('admin/add_employee', views.add_employee, name="add_employee"),
    path('admin/view_employee', views.view_employee, name="view_employee"),
    path('admin/all_leaves', views.all_leaves, name="all_leaves"),
    path('admin/pandding_leaves', views.pandding_leaves, name="pandding_leaves"),
    path('admin/approved_leaves', views.approved_leaves, name="approved_leaves"),
    path('admin/not_approved', views.not_approved, name="not_approved"),
    path('admin/login', views.login, name="login"),
]