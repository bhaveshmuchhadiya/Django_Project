from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin_index', views.index, name="index"),
    path('add_department', views.add_department, name="add_department"),
    path('view_department', views.view_department, name="view_department"),
    path('add_leave', views.add_leave, name="add_leave"),
    path('view_leave_type', views.view_leave_type, name="view_leave_type"),
    path('add_employee', views.add_employee, name="add_employee"),
    path('view_employee', views.view_employee, name="view_employee"),
    path('all_leaves', views.all_leaves, name="all_leaves"),
    path('pandding_leaves', views.pandding_leaves, name="pandding_leaves"),
    path('approved_leaves', views.approved_leaves, name="approved_leaves"),
    path('not_approved', views.not_approved, name="not_approved"),
]