from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import LoginForm, RegisterForm, RegisterCustomer

# Create your views here.
def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form["username"].value()
            password = form["password"].value()
            user = authenticate(username=username, password=password)
            if (user is not None):
                return redirect("/home")
    else:
        form = LoginForm()
    
    return render(request, "assignment/index.html", {"form":form})
    

def register(request):
    if (request.method == "POST"):
        form = RegisterForm(request.POST)
        if form.is_valid():
            choice = form["userType"].value()
            if choice == "customer":
                return redirect("/register_customer")
    else:
        form = RegisterForm()

    return render(request, "assignment/register.html", {"form":form})

def registerCustomer(request):
    if (request.method == "POST"):
        form = RegisterCustomer(request.POST)
        if form.is_valid():
            username = form["username"].value()
            password = form["password"].value()
            firstName = form["firstName"].value()
            surname = form["surname"].value()
            dob = form["dob"].value()
            phoneNum = form["phoneNum"].value()
            address = form["address"].value()
            billingAddress = form["billingAddress"].value()
            email = form["email"].value()
            
    else:
        form = RegisterCustomer()
    return render(request, "assignment/register_customer.html", {"form":form})

def home(request):
    return render(request, "assignment/home.html")