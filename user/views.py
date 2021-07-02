from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from user.models import User


def index(request):
    return render(request,"form_register.html")


def register(request):
    if request.method=="POST":
        name = request.POST['name']
        number = request.POST['number']
        email = request.POST['email']
        address = request.POST['address']
        college_name = request.POST['college_name']
        link = request.POST['link']
        file = request.FILES['file']
        if User.objects.filter(number=number,email=email).exists():
            messages.error(request,"Number or email are already registered")
            return redirect(index)
        else:
            user_data=User(name=name,number=number,email=email,address=address,college_name=college_name,link=link,file=file)
            user_data.save()
            messages.success(request,"Register Succesfully")
            return redirect(index)