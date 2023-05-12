from django.shortcuts import render,HttpResponse
from app.models import customuser
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.
def home(request):
    return render(request,"homepage.html")
def login1(request):
    return render(request,"newlogin.html")
def reg(request):
    return render(request,"sign.html")
def reg1(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        rpassword=request.POST.get("repassword")
        phone=request.POST.get("phone")
        if password!=rpassword:
            messages.success(request,"enter correct password")
            return render(request,"sign.html")
        elif customuser.objects.filter(email=email).first():
            messages.success(request,"email is already taken")
            return render(request,"sign.html")
        else:
            u=customuser.objects.create_user(firstname=name,username=email,email=email,password=password,phoneno=phone)
            u.save()
            login(request,u)
            messages.success(request,"details saved")
            return render(request,"newlogin.html")

def login2(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        if not email or not password:
            messages.success(request,"Both name and password is required")
            return render(request,"newlogin.html")
        else:
            u=authenticate(username=email,password=password)
            print("hii")
            if u is not None:
                login(request,u)
                print("loggggg")
                # return render(request,"accountantsignin.html")
                return HttpResponse("success")
            
             