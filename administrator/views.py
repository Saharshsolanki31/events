from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.
from administrator.models import ManagerLogin
from user.models import User


def manager_login(request):
    if 'userid' in request.session:
        user_data=User.objects.all()
        messages.success(request, "Already Logged In ")
        return render(request,"manager/manager_home.html",{"user_data":user_data})
    else:
        if request.method == "POST":
            userid = request.POST['userid']
            password = request.POST['password']
            if ManagerLogin.objects.filter(userid=userid, password=password).exists():
                request.session['userid'] = userid
                user_data = User.objects.all()
                messages.success(request, "login Success")
                return render(request, "manager/manager_home.html",{"user_data":user_data})
            else:
                messages.error(request, "login failed")
                return render(request, "manager_login.html")
        else:
            return render(request, "manager_login.html")

def logout(request):
    request.session.flush();
    messages.success(request,"logout")
    return render(request,'manager_login.html')
