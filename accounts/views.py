from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth #just link from django.shopping import attributes but here the model is already present in the database table
# Create your views here.
def register(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():#Checking if the username already exists
                messages.info(request,"Username taken")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"not correct password")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,"register.html")
def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:#if user is authorized user
            auth.login(request,user)#giving login access to the user
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return render(request,'login.html')
    else:
        return render(request,"login.html")
def logout(request):
    auth.logout(request)#inbuilt
    return redirect('/')