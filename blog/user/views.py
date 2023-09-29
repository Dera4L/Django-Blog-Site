from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")

        newUser = User(username =username)
        newUser.set_password(password)
        newUser.email = email

        newUser.save()
        login(request,newUser)
        messages.info(request,"You have successfully registered...")

        return redirect("/register/")
    context = {
            "form" : form
        }
    return render(request,"core/register.html",context)


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(username=username, password=password)
            if user is None:
                messages.info(request,"Your username and password don't match")
                return render(request,'core/login.html', context)
            messages.info(request, "You've succesfully Logged in")
            login(request, user)
            return redirect('/')
    else:
        form = LoginForm()
        
        return render(request, "core/login.html",context)
 
@login_required
def index(request):
    return render(request,"core/index.html")
    
    



