from django import forms

USER_CHOICES = [
    ("customer", "Customer"),
    ("insuranceProvider", "Insurance Provider"),
    ("government", "Government Agency"),
    ("lawFirm", "Law Firm"),
]

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    userType = forms.CharField(label="What account do you want to register?", widget=forms.RadioSelect(choices=USER_CHOICES))

class RegisterCustomer(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)
    firstName = forms.CharField(label="First Name", max_length=100)
    surname = forms.CharField(label="Surname", max_length=100)
    dob = forms.DateField(label="Date of Birth")
    phoneNum = forms.CharField(label="Phone number", max_length=100)
    address = forms.CharField(label="Home Address", max_length=128)
    billingAddress = forms.CharField(label="Billing Address", max_length=128)
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput, max_length=100)

class RegisterInsuranceProvider(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput, max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)
    phoneNum = forms.CharField(label="Phone number", max_length=100)
    address = forms.CharField(label="Home Address", max_length=128)
    billingAddress = forms.CharField(label="Billing Address", max_length=128)

class RegisterLawFirm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput, max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)
    phoneNum = forms.CharField(label="Phone number", max_length=100)
    address = forms.CharField(label="Home Address", max_length=128)
    billingAddress = forms.CharField(label="Billing Address", max_length=128)

class RegisterGovernment(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput, max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)
    address = forms.CharField(label="Home Address", max_length=128)
    billingAddress = forms.CharField(label="Billing Address", max_length=128)

class SellInsurance(forms.Form):
    title = forms.CharField(label="Insurance Name", max_length=100)
    coverage = forms.CharField(label = "Coverage", max_length=100)
    details = forms.CharField(label = "Details", max_length=200)
    cost = forms.FloatField(label = "Cost")