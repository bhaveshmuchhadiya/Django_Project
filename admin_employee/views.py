from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "admin_index.html")
def add_department(request):
    return render(request, "admin_add_department.html")
def view_department(request):
    return render(request, "admin_view_department.html")
def add_leave(request):
    return render(request, "admin_add_leave.html")
def view_leave_type(request):
    return render(request, "admin_view_leave_type.html")
def add_employee(request):
    return render(request, "admin_add_employee.html")
def view_employee(request):
    return render(request, "admin_view_employee.html")
def all_leaves(request):
    return render(request, "admin_all_leaves.html")
def pandding_leaves(request):
    return render(request, "admin_pandding_leaves.html")
def approved_leaves(request):
    return render(request, "admin_approved_leaves.html")