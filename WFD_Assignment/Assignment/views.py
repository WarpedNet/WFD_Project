from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
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
        if form.is_valid() and not UserModel.objects.filter(username = form["username"].value()).exists():
            user = UserModel(
                username = form["username"].value(),
                first_name = form["firstName"].value(),
                last_name = form["surname"].value(),
                email = form["email"].value(),
                address = form["address"].value(),
                billingAddress = form["billingAddress"].value(),
                accType = "customer"
            )
            user.set_password(form["password"].value())
            user.save()
            customer = Customer(user = user, dob = form["dob"].value(), phoneNum = form["phoneNum"].value())
            customer.save()

            return redirect("/login")
    else:
        form = RegisterCustomer()
    return render(request, "assignment/register_user.html", {"form":form, "ret":"/register_customer"})

def registerInsuranceProvider(request):
    if (request.method == "POST"):
        form = RegisterInsuranceProvider(request.POST)
        if form.is_valid() and not UserModel.objects.filter(username = form["username"].value()).exists():
            user = UserModel(
                username = form["username"].value(),
                email = form["email"].value(),
                address = form["address"].value(),
                billingAddress = form["billingAddress"].value(),
                accType = "insurance_provider"
            )
            user.set_password(form["password"].value())
            user.save()
            insuranceProvider = Insurance_Provider(
                user = user,
                phoneNum = form["phoneNum"].value()
            )
            insuranceProvider.save()
            return redirect("/login")
    else:
        form = RegisterInsuranceProvider()
    return render(request, "assignment/register_user.html", {"form":form, "ret":"/register_insurance_provider"})

def registerLawFirm(request):
    if (request.method == "POST"):
        form = RegisterLawFirm(request.POST)
        if form.is_valid() and not UserModel.objects.filter(username = form["username"].value()).exists():
            user = UserModel(
                username = form["username"].value(),
                email = form["email"].value(),
                address = form["address"].value(),
                billingAddress = form["billingAddress"].value(),
                accType = "law_firm"
            )
            user.set_password(form["password"].value())
            user.save()
            lawFirm = Law_Firm(
                user = user,
                phoneNum = form["phoneNum"].value()
            )
            lawFirm.save()
            return redirect("/login")
    else:
        form = RegisterLawFirm()
    return render(request, "assignment/register_user.html", {"form":form, "ret":"/register_law_firm"})

def registerGovernment(request):
    if (request.method == "POST"):
        form = RegisterGovernment(request.POST)
        if form.is_valid() and not UserModel.objects.filter(username = form["username"].value()).exists():
            user = UserModel(
                username = form["username"].value(),
                email = form["email"].value(),
                address = form["address"].value(),
                billingAddress = form["billingAddress"].value(),
                accType = "government"
            )
            user.set_password(form["password"].value())
            user.save()
            government = Government(
                user = user
            )
            government.save()
            return redirect("/login")
    else:
        form = RegisterGovernment()
    return render(request, "assignment/register_user.html", {"form":form, "ret":"/register_government"})
    


def home(request):
    if (not request.user.is_authenticated):
        return redirect("/login")
    
    if (request.user.accType == "customer"):
        customer = Customer.objects.get(user = request.user)
        insuranceCoverage = Purchase_Order.objects.filter(customer = customer)
        claims = Claims.objects.filter(customer = customer)
        return render(request, "assignment/home.html", {"user":request.user, "insuranceCoverage":insuranceCoverage, "claims":claims})
    return render(request, "assignment/home.html", {"user":request.user})
        

def account(request):
    if (not request.user.is_authenticated):
        return redirect("/login")

    if (request.method == "POST"):
        user = UserModel.objects.get(username = request.user.username)
        if (request.user.accType == "customer"):
            customer = Customer.objects.get(user = user)
            form = RegisterCustomer(request.POST)
            if (form.is_valid()):
                user.username = form["username"].value()
                user.first_name = form["firstName"].value()
                user.last_name = form["surname"].value()
                user.email = form["email"].value()
                user.address = form["address"].value()
                user.billingAddress = form["billingAddress"].value()
                user.set_password(form["password"].value())
                user.save()
                customer.user = user
                customer.dob = form["dob"].value()
                customer.phoneNum = form["phoneNum"].value()
                customer.save()
        elif (request.user.accType == "insurance_provider"):
            insurance_provider = Insurance_Provider.objects.get(user)
            form = RegisterInsuranceProvider(request.POST)
            if (form.is_valid()):
                user.username = form["username"].value()
                user.email = form["email"].value()
                user.address = form["address"].value()
                user.billingAddress = form["billingAddress"].value()
                user.set_password(form["password"].value())
                user.save()
                insurance_provider.user = user,
                insurance_provider.phoneNum = form["phoneNum"].value()
                insurance_provider.save()

        elif (request.user.accType == "law_firm"):
            law_firm = Law_Firm.objects.get(user)
            form = RegisterLawFirm(request.POST)
            if (form.is_valid()):
                user.username = form["username"].value()
                user.email = form["email"].value()
                user.address = form["address"].value()
                user.billingAddress = form["billingAddress"].value()
                user.set_password(form["password"].value())
                user.save()
                law_firm.user = user,
                law_firm.phoneNum = form["phoneNum"].value()
                law_firm.save()

        elif (request.user.accType == "government"):
            government = Government.objects.get(user = user)
            form = RegisterGovernment(request.POST)
            if (form.is_valid()):
                user.username = form["username"].value()
                user.email = form["email"].value()
                user.address = form["address"].value()
                user.billingAddress = form["billingAddress"].value()
                user.set_password(form["password"].value())
                user.save()
                government.user = user
                government.save()
        return redirect("/login")
    else:
        if (request.user.accType == "customer"):
            customer = Customer.objects.get(user = request.user)
            form = RegisterCustomer(
                initial={
                    'username':request.user.username,
                    'firstName':request.user.first_name,
                    'surname':request.user.last_name,
                    'dob':customer.dob,
                    'phoneNum':customer.phoneNum,
                    'address':request.user.address,
                    'billingAddress':request.user.billingAddress,
                    'email':request.user.email
                }
            )
        elif (request.user.accType == "law_firm"):
            law_firm = Law_Firm.objects.get(user = request.user)
            form = RegisterLawFirm(
                initial={
                    'username':request.user.username,
                    'email':request.user.email,
                    'phoneNum':law_firm.phoneNum,
                    'address':request.user.address,
                    'billingAddress':request.user.billingAddress
                }
            )
        elif (request.user.accType == "insurance_provider"):
            insurance_provider = Insurance_Provider.objects.get(user = request.user)
            form = RegisterInsuranceProvider(
                initial={
                    'username':request.user.username,
                    'email':request.user.email,
                    'phoneNum':insurance_provider.phoneNum,
                    'address':request.user.address,
                    'billingAddress':request.user.billingAddress
                }
            )
        elif (request.user.accType == "government"):
            form = RegisterGovernment(
                initial={
                    'username':request.user.username,
                    'email':request.user.email,
                    'address':request.user.address,
                    'billingAddress':request.user.billingAddress
                }
            )

    return render(request, "assignment/account.html", {"user":request.user, "form":form})

def view_insurance(request):
    if (not request.user.is_authenticated):
        return redirect("/login")
    
    insurance = Insurance.objects.all()
    return render(request, "assignment/view_insurance.html", {"user":request.user, "insurances":insurance})

def sell_insurance(request):
    if (not request.user.is_authenticated or request.user.accType != "insurance_provider"):
        return redirect("/login")
    
    if (request.method == "POST"):
        form = SellInsurance(request.POST)
        insurance_provider = Insurance_Provider.objects.get(user = request.user)
        if form.is_valid():
            insurance = Insurance(
                provider = insurance_provider,
                title = form["title"].value(),
                coverage = form["coverage"].value(),
                details = form["details"].value(),
                cost = form["cost"].value(),
            )
            insurance.save()
            return redirect("/sell_insurance")
    else:
        form = SellInsurance()
    return render(request, "assignment/sell_insurance.html", {"user":request.user, "form":form})

def make_purchase_order(request, insuranceID):
    insurance = Insurance.objects.get(pk=insuranceID)
    customer = Customer.objects.get(user = request.user)
    po = Purchase_Order(
        customer = customer,
        insurance = insurance
    )
    po.save()
    return redirect("/view_insurance")

def make_claim(request):
    if (not request.user.is_authenticated or request.user.accType != "customer"):
        return redirect("/login")
    customer = Customer.objects.get(user = request.user)
    if (request.method == "POST"):
        form = MakeClaim(request.POST, customer = customer)
        insurance = Insurance.objects.get(pk = form["insurance"].value())
        if form.is_valid():
            claim = Claims(
                insurance = insurance,
                customer = customer,
                date = form["date"].value(),
                third_parties = form["third_parties"].value(),
                details = form["details"].value(),
            )
            claim.save()
            return redirect("/home")
    else:
        form = MakeClaim(customer = customer)
    return render(request, "assignment/make_claim.html", {"user":request.user, "form":form})

def logout_page(request):
    logout(request)
    return redirect("/login")