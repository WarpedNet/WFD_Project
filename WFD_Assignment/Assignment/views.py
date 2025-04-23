from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import *
from .forms import LoginForm, RegisterForm, RegisterCustomer, RegisterInsuranceProvider, RegisterLawFirm, RegisterGovernment

# Create your views here.
def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form["username"].value()
            password = form["password"].value()
            user = authenticate(username=username, password=password)
            if (user is not None):
                login(request, user)
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
            elif choice == "insuranceProvider":
                return redirect("/register_insurance_provider")
            elif choice == "lawFirm":
                return redirect("/register_law_firm")
            elif choice == "government":
                return redirect("/register_government")
    else:
        form = RegisterForm()

    return render(request, "assignment/register.html", {"form":form})

def registerCustomer(request):
    if (request.method == "POST"):
        form = RegisterCustomer(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form["username"].value(),
                form["email"].value(),
                form["password"].value()
            )
            user.first_name = form["firstName"].value()
            user.last_name = form["surname"].value()
            user.dob = form["dob"].value()
            user.phone_num = form["phoneNum"].value()
            user.address = form["address"].value()
            user.billing_address = form["billingAddress"].value()
            user.accType = "customer"
            user.save()
            return redirect("/login")
    else:
        form = RegisterCustomer()
    return render(request, "assignment/register_user.html", {"form":form})

def registerInsuranceProvider(request):
    if (request.method == "POST"):
        form = RegisterInsuranceProvider(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form["username"].value(),
                form["email"].value(),
                form["password"].value()
            )
            user.phone_num = form["phoneNum"].value()
            user.address = form["address"].value()
            user.billing_address = form["billingAddress"].value()
            user.accType = "insurance_provider"
            user.save()
            return redirect("/login")
    else:
        form = RegisterInsuranceProvider()
    return render(request, "assignment/register_user.html", {"form":form})

def registerLawFirm(request):
    if (request.method == "POST"):
        form = RegisterLawFirm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form["username"].value(),
                form["email"].value(),
                form["password"].value()
            )
            user.phone_num = form["phoneNum"].value()
            user.address = form["address"].value()
            user.billing_address = form["billingAddress"].value()
            user.accType = "law_firm"
            user.save()
            return redirect("/login")
    else:
        form = RegisterLawFirm()
    return render(request, "assignment/register_user.html", {"form":form})

def registerGovernment(request):
    if (request.method == "POST"):
        form = RegisterGovernment(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form["username"].value(),
                form["email"].value(),
                form["password"].value()
            )
            user.address = form["address"].value()
            user.billing_address = form["billingAddress"].value()
            user.accType = "government"
            user.save()
            return redirect("/login")
    else:
        form = RegisterGovernment()
    return render(request, "assignment/register_user.html", {"form":form})
    


def home(request):
    if (request.user.is_authenticated):
        return render(request, "assignment/home.html", {"user":request.user})
    else:
        return redirect("/login")