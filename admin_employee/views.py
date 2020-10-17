from django.shortcuts import render,redirect
from django.http import HttpResponse
import mysql.connector as mydb
# Create your views here.

con = mydb.connect(host="localhost", user="root", password="", database="django_db")
print("successfully coonected with databse...")
cur = con.cursor()

def index(request):
    return render(request, "admin_index.html")
def login(request):
    return render(request, "admin_login.html")
def add_department(request):
    return render(request, "admin_add_department.html")
def insert_department(request):
    if request.method == 'POST':
        dept_code = request.POST['dept_code']
        dept_name = request.POST['dept_name']
        dept_cre_date = request.POST['dept_cre_date']
        cur.execute("insert into department(department_code,department_name,creation_date) values ('{}','{}','{}')".format(dept_code,dept_name,dept_cre_date))
        con.commit()
        return redirect(view_department)
    else:
        return redirect(add_department)
def view_department(request):
    sel = cur.execute("select * from department")
    data = cur.fetchall()
    return render(request,'admin_view_department.html',{'data':data})
def add_leave(request):
    return render(request, "admin_add_leave.html")
def insert_leave(request):
    if request.method == 'POST':
        leave_type = request.POST['leave_type']
        des = request.POST['description']
        cre_date = request.POST['cre_date']
        cur.execute("insert into leave_type(leave_type,description,creation_date) values ('{}','{}','{}')".format(leave_type,des,cre_date))
        con.commit()
        return redirect(view_leave_type)
    else:
        redirect(add_leave)
def view_leave_type(request):
    sel = cur.execute("select * from leave_type")
    data = cur.fetchall()
    return render(request, "admin_view_leave_type.html",{"data":data})
def add_employee(request):
    sel_dep = cur.execute("select department_name from department")
    data = cur.fetchall()
    return render(request, "admin_add_employee.html",{"data":data})
def insert_employee(request):
    if request.method == 'POST':
        f_name = request.POST['first_name']
        s_name = request.POST['second_name']
        l_name = request.POST['last_name']
        gender = request.POST['gender']
        dept = request.POST['department']
        b_date = request.POST['birth_date']
        address = request.POST['address']
        city = request.POST['city']
        email = request.POST['email']
        mno = request.POST['mnumber']
        unm= request.POST['username']
        pas = request.POST['password']
        cur.execute("insert into employee(first_name,second_name,last_name,gender,department,birth_date,address,city,mail_id,mobile,username,password) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(f_name,s_name,l_name,gender,dept,b_date,address,city,email,mno,unm,pas))
        con.commit()
        return redirect(view_employee)
    else:
        return redirect(add_employee)
def view_employee(request):
    sel = cur.execute("select * from employee")
    data = cur.fetchall()
    return render(request, "admin_view_employee.html",{"data":data})
def all_leaves(request):
    return render(request, "admin_all_leaves.html")
def pandding_leaves(request):
    return render(request, "admin_pandding_leaves.html")
def approved_leaves(request):
    return render(request, "admin_approved_leaves.html")
def not_approved(request):
    return render(request, "admin_notapproved_leaves.html")