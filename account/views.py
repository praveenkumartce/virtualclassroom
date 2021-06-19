from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.views.generic import CreateView
from django.contrib.messages import constants as messages

from .models import *
from .forms import FacultyReg,StudentReg


def AddFaculty(request):
    if not request.user.is_superuser:
        return redirect('admin_login')
    error=""
    if request.method=='POST':
        uname=request.POST['uname']
        psd=request.POST['psd']
        id=request.POST['faculty_id']
        dept=request.POST['faculty_dept']
        deg=request.POST['faculty_deg']
        name=request.POST['faculty_name']
        since=request.POST['since']
        if request.method=='POST':
            if User.objects.filter(username=uname,password=psd).exists():
                print("username taken Already")
                error="yes"
            else:
                    user = User.objects.create_user(username=uname, password=psd)
                    user.is_faculty = True
                    user.save()
                    print("user created")
                    faculty = Faculty.objects.create(user=user,faculty_name = name,faculty_id = id,fac_dept =Department.objects.get(dep_id = dept),faculty_deg = deg,since = since)
                    faculty.save()
                    dep=Department.objects.get(dep_id=dept)
                    print(dep.faculty_nos)
                    dep.faculty_nos += 1
                    dep.save()
                    error="no"
            print(error)
    d={'error':error}
    return render(request,'add_faculty.html',d)

# Create your views here.

def AddStudent(request):
    if not request.user.is_superuser:
        return redirect('admin_login')
    error=""
    if request.method=='POST':
        uname=request.POST['uname']
        psd=request.POST['psd']
        id=request.POST['student_id']
        dept=request.POST['student_dept']
        name=request.POST['student_name']
        since=request.POST['since']
        if request.method=='POST':
            if User.objects.filter(username=uname,password=psd).exists():
                print("username taken Already")
                error="yes"
            else:
                    user=User.objects.create_user(username=uname, password=psd)
                    user.is_student = True
                    user.save()
                    student = Student.objects.create(user=user,student_name = name,student_id = id,stud_dept = Department.objects.get(dep_id=dept),join_date = since)
                    dep=Department.objects.get(dep_id=dept)
                    print(dep.student_nos)
                    dep.student_nos+=1
                    dep.save()
                    student.save()
                    error="no"
            print(error)
    d={'error':error}
    return render(request,'add_student.html',d)

def ViewFaculty(request):
    if not request.user.is_superuser:
        return redirect('admin_login')
    else:
        fac= Faculty.objects.all()
        p={'fac':fac}
        return render(request,'view_faculty.html',p)


def ViewStudent(request):
    if not request.user.is_superuser:
        return redirect('admin_login')
    else:
        stud= Student.objects.all()
        p={'stud':stud}
        return render(request,'view_students.html',p)

