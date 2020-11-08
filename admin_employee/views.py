from django.http import HttpResponse
from django.shortcuts import render,redirect
import mysql.connector as mydb
import datetime
import pandas as pd
# Create your views here.

con = mydb.connect(host="localhost", user="root", password="", database="django_db")
print("successfully coonected with databse...")
cur = con.cursor()

def index(request):
    if request.session.has_key('username'):
        cur.execute("select emp_id from employee")
        data = cur.fetchall()
        print(data)
        count = 0
        for i in data:
            count = count+1
        cur.execute("select id from department")
        d_data = cur.fetchall()
        print()
        d_count = 0
        for i in d_data:
            d_count +=1
        cur.execute("select l_id from leaves")
        t_data = cur.fetchall()
        print()
        t_count = 0
        for i in t_data:
            t_count +=1
        # emp_data= data
        return render(request, "admin_index.html",{"emp_data":count,"d_data":d_count,"t_data":t_count})
    else:
        return redirect(login)
def login(request):
    if request.session.has_key('username'):
        return redirect(index)
    else:
        return render(request, "admin_login.html")
def login_process(request):
    user = request.POST['username'] 
    pas = request.POST['password'] 
    # print(user,pas)
    sel = cur.execute("select username,password from admin")
    data = cur.fetchall()
    # print(data)
    # print(data[1])
    for i in data:
        print(i)
        if (user , pas) == i:
            request.session['username'] = user
            return redirect(index)
    return redirect(login)
    
def add_department(request):
    if request.session.has_key('username'):
        return render(request, "admin_add_department.html")
    else:
        return redirect(login)
def insert_department(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            dept_code = request.POST['dept_code']
            dept_name = request.POST['dept_name']
            dept_cre_date = request.POST['dept_cre_date']
            cur.execute("insert into department(department_code,department_name,creation_date) values ('{}','{}','{}')".format(dept_code,dept_name,dept_cre_date))
            con.commit()
            return redirect(view_department)
        # else:
        #     print(id)
        #     sel = cur.execute("select * from department where id='{}'".format(id))
        #     data = cur.fetchall()
        #     print(data)
        #     return render(request, "admin_update_department.html",{"data":data})
    else:
        return redirect(login)    
        
def get_department(request,id):
    if request.session.has_key('username'):
        print(id)
        sel = cur.execute("select * from department where id='{}'".format(id))
        data = cur.fetchall()
        print(data)
        return render(request, "admin_update_department.html",{"data":data})
    else:
        return redirect(login)
def update_department_process(request):
    if request.session.has_key('username'):
        d_name = request.POST['dept_name']
        d_id = request.POST['d_id']
        cur.execute("update department set department_name = '{}' where id = '{}'".format(d_name,d_id))
        con.commit()
        return redirect(view_department)
    else:
        return redirect(login)
def delete_department(request,id):
    if request.session.has_key('username'):
        cur.execute("delete from department where id ='{}'".format(id))
        con.commit()
        return redirect(view_department)
    else:
        return redirect(login)
def view_department(request):
    if request.session.has_key('username'):
        sel = cur.execute("select * from department")
        data = cur.fetchall()
        print(data)
        return render(request,'admin_view_department.html',{'data':data})
    else:
        return redirect(login)
def add_leave(request):
    if request.session.has_key('username'):
        return render(request, "admin_add_leave.html")
    else:
        return redirect(login)
def insert_leave(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            leave_type = request.POST['leave_type']
            des = request.POST['description']
            cre_date = request.POST['cre_date']
            cur.execute("insert into leave_type(leave_type,description,creation_date) values ('{}','{}','{}')".format(leave_type,des,cre_date))
            con.commit()
            return redirect(view_leave_type)
        # else:
        #     print(id)
        #     cur.execute("select * from leave_type where id = '{}'".format(id))
        #     data = cur.fetchall()
        #     return render(request,"admin_update_leave_type.html",{"data":data})
    else:
        return redirect(login)
def get_leave(request,id):
    if request.session.has_key('username'):
        print(id)
        cur.execute("select * from leave_type where id = '{}'".format(id))
        data = cur.fetchall()
        return render(request,"admin_update_leave_type.html",{"data":data})
    else:
        return redirect(login)
def update_leave(request):
    if request.session.has_key('username'):
        l_type = request.POST['leave_type']
        des = request.POST['description']
        l_id = request.POST['l_id']
        cur.execute("update leave_type set leave_type = '{}', description = '{}' where id = '{}' ".format(l_type,des,l_id))
        con.commit()
        return redirect(view_leave_type)
    else:
        return redirect(login)
def delete_leave_type(request,id):
    if request.session.has_key('username'):
        cur.execute("delete from leave_type where id ='{}'".format(id))
        con.commit()
        return redirect(view_leave_type)
    else:
        return redirect(login)
def view_leave_type(request):
    if request.session.has_key('username'):
        sel = cur.execute("select * from leave_type")
        data = cur.fetchall()
        return render(request, "admin_view_leave_type.html",{"data":data})
    else:
        return redirect(login)
def add_employee(request):
    if request.session.has_key('username'):
        sel_dep = cur.execute("select department_name from department")
        data = cur.fetchall()
        return render(request, "admin_add_employee.html",{"data":data})
    else:
        return redirect(login)

def insert_employee(request):
    if request.session.has_key('username'):
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
        # else:
            # cur.execute("select * from employee where emp_id = '{}'".format(id))
            # data = cur.fetchall()
            # cur.execute("select * from  department")
            # dept = cur.fetchall()
            # return render(request, "admin_update_employee.html",{"data":data,"dept":dept})
    else:
        return redirect(login)
def get_employee(request,id):
    if request.session.has_key('username'):
        cur.execute("select * from employee where emp_id = '{}'".format(id))
        data = cur.fetchall()
        cur.execute("select * from  department")
        dept = cur.fetchall()
        return render(request, "admin_update_employee.html",{"data":data,"dept":dept})
    else:
        return redirect(login)
def update_employee(request):
    if request.session.has_key('username'):
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
        e_id=request.POST['e_id']
        cur.execute("update employee set first_name='{}',second_name='{}',last_name='{}',gender='{}',department='{}',birth_date='{}',address='{}',city='{}',mail_id='{}',mobile='{}' where emp_id= '{}'".format(f_name,s_name,l_name,gender,dept,b_date,address,city,email,mno,e_id))
        con.commit()
        return redirect(view_employee)
    else:
        return redirect(login)
def delete_employee(request,id):
    if request.session.has_key('username'):
        cur.execute("delete from leaves where emp_id= '{}'".format(id))
        cur.execute("delete from employee where emp_id= '{}'".format(id))
        con.commit()
        return redirect(view_employee)
    else:
        return redirect(login)
def view_employee(request):
    if request.session.has_key('username'):
        sel = cur.execute("select * from employee")
        data = cur.fetchall()
        return render(request, "admin_view_employee.html",{"data":data})
    else:
        return redirect(login)

def employee_detail(request,id):
    if request.session.has_key('username'):
        cur.execute("select * from employee where emp_id = '{}'".format(id))
        data = cur.fetchall()
        return render(request, "employee_details.html",{'data':data})
    else:
        return redirect(login)
def all_leaves(request):
    # al = request.GET['admin/all_leaves']
    if request.session.has_key('username'):
        sel = cur.execute("select * from employee inner join leaves on employee.emp_id=leaves.emp_id")
        data = cur.fetchall()
        # print(data)
        # print(al)
        # if():
        return render(request, "admin_all_leaves.html",{"data":data})
    else:
        return redirect(login)
def leave_action(request,id):
    if request.session.has_key('username'):
        cur.execute("select * from employee inner join leaves on employee.emp_id=leaves.emp_id where employee.emp_id = '{}' and leaves.status='pendding'".format(id))
        data = cur.fetchall()
        return render(request, "leave_action.html",{'data':data})
    else:
        return redirect(login)
def action(request):
    if request.session.has_key('username'):
        pdate = request.POST['p_date']
        # dt = date.pdate()
        # now = datetime.strptime("%b %d %y")
        # abc = datetime.today().strftime('%y-%m-%d')
        # print(abc)
        # print(arrow.now().format('YYYY-MM-DD'))
        # print(pd.to_datetime(pdate).date())
        dt = pd.to_datetime(pdate).date()
        status = request.POST['status']
        cur.execute("update leaves set status='{}' where from_date = '{}'".format(status,dt))
        con.commit()
        return redirect(all_leaves)
    else:
        return redirect(login)
def pandding_leaves(request):
    if request.session.has_key('username'):
        cur.execute("select * from employee inner join leaves on employee.emp_id=leaves.emp_id where leaves.status = 'pendding'")
        data = cur.fetchall()
        return render(request, "admin_pandding_leaves.html",{'data':data})
    else:
        return redirect(login)
def approved_leaves(request): 
    if request.session.has_key('username'): 
        # sel = cur.execute("select * from leaves where status = 'approved'")
        # data = cur.fetchall()
        cur.execute("select * from employee inner join leaves on employee.emp_id=leaves.emp_id where leaves.status = 'approved'")
        data = cur.fetchall()
        return render(request, "admin_approved_leaves.html",{"data":data})
    else:
        return redirect(login)
def not_approved(request):
    if request.session.has_key('username'):
        cur.execute("select * from employee inner join leaves on employee.emp_id=leaves.emp_id where leaves.status = 'disapprove'")
        data = cur.fetchall()
        return render(request, "admin_approved_leaves.html",{"data":data})
    else:
        return redirect(login)
def logout(request):
    del request.session['username']
    response = redirect(login)
    return response
# def change_password(request):
#     return render(request, "change_pass_employee.html")