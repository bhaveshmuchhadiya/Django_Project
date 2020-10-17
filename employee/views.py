from django.shortcuts import render,redirect
from django.http import HttpResponse
import mysql.connector as mydb

con = mydb.connect(host="localhost", user="root", password="", database="django_db")
print("successfully coonected with databse...")
cur = con.cursor()


def index(request):
    return render(request,"index.html")
def login(request):
    return render(request, "login.html")
def change_pass(request):
    return render(request, "change_pass_employee.html")
def leave_apply(request):
    if request.session.has_key('username'):
        return render(request, "leave_apply.html")
    else:
        return render(request, 'login.html')
def leave_details(request):
    if request.session.has_key('username'):
        return render(request, "leave_details.html")
    else:
        return render(request, 'login.html')
def home(request):
    if request.session.has_key('username'):
        return render(request, 'user_home.html')
    else:
        return render(request, 'login.html')
def process(request):
    user = request.POST['txt1'] 
    request.session['username'] = user
    response = redirect(home)
    return response
def logout(request):
    del request.session['username']
    response = redirect(login)
    return response