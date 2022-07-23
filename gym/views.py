from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def Login(request):
    error = ""
    if request.method=='post':
        username = request.post['uname']
        password = request.post['pwd']
        user = authenticate(username=username,password=password)
        try:
            if user.is_staff:
                login(request,user)
                error ="no"
            else:
                error = 'Yes'
        except:
            error='Yes'
    d= {'error':error}
    return render(request,'login.html',d)
def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')

def AboutUs(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

