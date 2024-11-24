from django.shortcuts import render
from django.shortcuts import render , redirect , HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from home.models import course
# Create your views here.

def myadmin(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        key_user = authenticate(request,username=username,password=password )
        if key_user is not None:
            login(request,key_user)
            if key_user.is_superuser:
                return redirect('admindashboard')
            # else:
                
    return render(request,"adminlogin.html")


def admindash(request):
    total = course.objects.all().count()
    teacher = User.objects.all().count()
    # print(teacher)
    context = {
       'total': total,
       'teacher':teacher
   }
    return render(request,"admindeshboard.html",context )

def allcourse(request):
    cour= course.objects.all()
    context ={
        'cour' : cour
    }
    return render(request,"admintemplte/admincourse.html",context)