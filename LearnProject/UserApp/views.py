from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from FlagApp.models import *
from .models import *
from .form import *
from django.contrib import messages


def index(request):
    return render(request, "userapp/index.html")


def profile(request):
    user = CustomUser.objects.filter(id=request.user.id).first()
    recordsFlag = Records.objects.filter(user=request.user).order_by("-score")[:5]
    deleteRecordsFlag = Records.objects.filter(user=request.user).order_by("-score")[5:]
    recordsCapital = Records1.objects.filter(user=request.user).order_by("-score")[:5]
    deleteRecordsCapital = Records1.objects.filter(user=request.user).order_by("-score")[5:]
    
    for i in deleteRecordsFlag:
        i.delete()
    
    for i in deleteRecordsCapital:
        i.delete()    
        
    context={
        "user":user,
        "recordsFlag":recordsFlag,
        "recordsCapital":recordsCapital,
        
    }
   
    return render(request, "userapp/profile.html", context)


def settings(request):
    return render(request, "userapp/settings.html")


def records(request):
    return render(request, "userapp/records.html")

def login(request):
    
    if request.method == "POST":
        if 'login-submit' in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            if username and password:
                user = authenticate(request, username=username, password=password)
                if user:
                    auth_login(request, user)
                    return redirect("home")
                else:
                    return redirect("home")
        else:
            if 'register-submit' in request.POST:
                
                username = request.POST.get("username")
                password = request.POST.get("password")
                email = request.POST.get("email")
                avatar = request.FILES.get("avatar")

                if len(password) < 8 :
                    return redirect("login")
                if username and password and email:
                    new_user = CustomUser.objects.create_user(username=username, email=email, password=password)
                    new_user.avatar = avatar  # Avatar dosyasını atayın
                    new_user.save()  #
                    messages.add_message(request, messages.WARNING, f"Registration Successful. Please log in")

                    return redirect("login")
    return render(request, "userapp/login.html")            

def log_out(request):
    logout(request)
    return redirect("home")

        



    