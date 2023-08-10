from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from addstudent.models import student
from django.core import serializers
from django.contrib import messages

# Create your views here.
def ind(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        name = request.POST.get('usrname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        confirm_password = request.POST.get('re_pass')
        myuser=User.objects.create_user(name, email, password)
        myuser.save()
        u1 = auth.authenticate(username=name1, password=passw1)
        if u1 is not None:
            # A backend authenticated the credentials
            auth.login(request, u1)
            return redirect('/select/')
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        name1 = request.POST.get('name')
        passw1 = request.POST.get('pass')
        u1 = auth.authenticate(username=name1, password=passw1)
        if u1 is not None:
            # A backend authenticated the credentials
            auth.login(request, u1)
            messages.info(request, 'login successful!')
            return redirect('/select/')
        else:
            # No backend authenticated the credentials
            return render(request, 'index.html')
    return render(request, 'index.html')

def select(request):
    if request.method=="POST":
        return redirect('/attendance/')
    return render(request, 'selector.html')

def addstudent1(request):
    if request.method=="POST":
        try:
            name=request.POST.get('name')
            enroll=request.POST.get('enroll')
            course=request.POST.get('val1')
            year=request.POST.get('val2')
            sem=request.POST.get('val3')
            inst=student.objects.create(name=name,enrollment=enroll,course=course,year=year,semester=sem)
            inst.save()
        except:
            messages.info(request, 'enrollment number is already in the list!')
    data = serializers.serialize("python", student.objects.all().order_by('enrollment'))
    context={
        'data':data,
    }
    return render(request, 'attendence.html', context)

def storeattendance(request):
    data = serializers.serialize("python", student.objects.all().order_by('enrollment'))
    context={
        'data':data,
    }
    if request.method=="POST":
        for i,j in list(enumerate(student.objects.all())):
            getatt=request.POST.get(j.enrollment)
            if getatt=="present":
                stu=student.objects.get(enrollment=j.enrollment)
                stu.attendance='True'
                stu.save()
            elif getatt=="absent":
                stu=student.objects.get(enrollment=j.enrollment)
                stu.attendance='False'
                stu.save()
    return render(request, 'attendence.html',context)