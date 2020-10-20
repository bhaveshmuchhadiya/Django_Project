from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/admin_index', views.index, name="index"),
    path('admin/add_department', views.add_department, name="add_department"),
    # path('admin/update_department/<int:id>', views.update_department, name="update_department"),
    path('admin/update_department_process', views.update_department_process, name="update_department_process"),
    path('admin/insert_department', views.insert_department, name="insert_department"),
    path('admin/update_department/<int:id>', views.insert_department, name="insert_department"),
    path('admin/delete_department/<int:id>', views.delete_department, name="insert_department"),
    path('admin/view_department', views.view_department, name="view_department"),
    path('admin/add_leave', views.add_leave, name="add_leave"),
    path('admin/update_leave', views.update_leave, name="update_leave"),
    path('admin/insert_leave', views.insert_leave, name="insert_leave"),
    path('admin/update_leave/<int:id>', views.insert_leave, name="insert_leave"),
    # path('admin/update_leave', views.update_leave, name="insert_leave"),
    path('admin/delete_leave_type/<int:id>', views.delete_leave_type, name="delete_leave_type"),
    path('admin/view_leave_type', views.view_leave_type, name="view_leave_type"),
    path('admin/add_employee', views.add_employee, name="add_employee"),
    path('admin/insert_employee', views.insert_employee, name="insert_employee"),
    path('admin/update_employee/<int:id>', views.insert_employee, name="update_employee"),
    path('admin/update_employee', views.update_employee, name="update_employee"),
    path('admin/delete_employee/<int:id>', views.delete_employee, name="delete_employee"),
    path('admin/view_employee', views.view_employee, name="view_employee"),
    path('admin/all_leaves', views.all_leaves, name="all_leaves"),
    path('admin/pandding_leaves', views.pandding_leaves, name="pandding_leaves"),
    path('admin/approved_leaves', views.approved_leaves, name="approved_leaves"),
    path('admin/not_approved', views.not_approved, name="not_approved"),
    path('admin/login', views.login, name="login"),
]