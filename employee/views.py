from django.shortcuts import render,redirect
from django.http import HttpResponse
import mysql.connector as mydb
from datetime import date
# from tkinter import *
# from tkinter import messagebox 
from pymsgbox import *

con = mydb.connect(host="localhost", user="root", password="", database="django_db")
print("successfully coonected with databse...")
cur = con.cursor()

def master(request):
    user = cur.execute("select * from employee")
    data = cur.fetchall()
    return data

def index(request):
   return render(request,"index.html")
def change_pass(request):
    if request.session.has_key('username'):
        return render(request, "change_pass_employee.html")
    else:
        return redirect(login)
def leave_apply(request):
    if request.session.has_key('username'):
        user = request.session['username']
        cur.execute("select emp_id from employee where mail_id = '{}'".format(user))
        user_id = cur.fetchone()
        user_id = user_id[0]
        # print(user_id[0])
        today = date.today()
        print(today)
        now = today.strftime('%d-%m-%y')
        sel = cur.execute("select * from leave_type")
        leave_type = cur.fetchall()
        return render(request, "leave_apply.html",{"leave_type":leave_type,'user_id':user_id,"today":now})
    else:
        return render(request, 'login.html')
def leave_insert(request):
    if request.method == 'POST':
        l_type = request.POST['l_type']
        f_date = request.POST['from_date']
        t_date = request.POST['to_date']
        des = request.POST['description']
        p_date = request.POST['p_date']
        e_id = request.POST['e_id']
        status = request.POST['status']
        print(l_type)
        cur.execute("insert into leaves(leave_type,from_date,to_date,description,posting_date,status,emp_id) values ('{}','{}','{}','{}','{}','{}','{}')".format(l_type,f_date,t_date,des,p_date,status,e_id))
        con.commit()
        # con.close()
        return redirect(leave_details)
    else:
        return redirect(leave_apply)    
def leave_details(request):
    if request.session.has_key('username'):
        print(request.session['username'])
        user = request.session['username']
        sel = cur.execute("select * from leaves where emp_id = (select emp_id from employee where mail_id ='{}')".format(user))
        data = cur.fetchall()
        print(data)
        return render(request, "leave_details.html",{"data":data})
    else:
        return render(request, 'login.html')
def home(request):
    if request.session.has_key('username'):
        return render(request, 'user_home.html')
    else:
        return render(request, 'login.html')
def login(request):
    if request.session.has_key('username'):
        return redirect(home)   
    else:
        return render(request, "login.html")
def process(request):
    user = request.POST['username'] 
    pas = request.POST['password'] 
    sel = cur.execute("select mail_id,password from employee")
    data = cur.fetchall()
    print(data)
    for i in data:
        print(i)
        # for j in data:
        # print(data[2])
        if (user , pas) == i:
            request.session['username'] = user
            return render(request, "user_home.html")
    return redirect(login)
            
def logout(request):
    if request.session.has_key('username'):
        del request.session['username']
        response = redirect(login)
        return response
    else:
        return render(request, "login.html")

def forgot_password(request):
    if request.session.has_key('username'):
        old_pas = request.POST['old_password']
        # print(old_pas)
        new_pas = request.POST['new_password']
        con_pas = request.POST['con_password']
        user = request.session['username']
        cur.execute("select password from employee where emp_id = (select emp_id from employee where mail_id = '{}') ".format(user))
        user_data = cur.fetchone()
        # print(user_data)
        # print(old_pas)
        if(user_data[0] == old_pas):
            print(user_data[0])
            if(new_pas == con_pas):
                cur.execute("update employee set password = '{}' where emp_id =(select emp_id from employee where mail_id = '{}') ".format(con_pas,user))
                con.commit()
                return redirect(home)
        else:
            # # top = Tk()  
            # # top.geometry("100x100")  
            # messagebox.showerror("password","Wrong Password")         
  
            # # top.mainloop()  
            alert(text='Wrong Password', title='Wrong Password', button='OK')
            return redirect(home)
    else:
        return redirect(login)