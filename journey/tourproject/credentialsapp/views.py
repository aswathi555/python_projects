from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

# Create your views here.
def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        pswd=request.POST['password']
        cpswd=request.POST['confpassword']
        mail=request.POST['email']
        if pswd==cpswd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,"Email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=mail,password=pswd)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password mismatch")
            return redirect('register')
        print("User Registered")
        return redirect('/')
    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def about(request):
    return render(request,"about.html")
