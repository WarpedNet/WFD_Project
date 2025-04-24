from django.db import models
from django.contrib.auth.models import AbstractUser
# from .forms import RegisterCustomer

# Create your models here.
class UserModel(AbstractUser):
    USER_TYPES = (
        ("CUSTOMER", "customer"),
        ("LAW_FIRM", "law_firm"),
        ("INSURANCE_PROVIDER", "insurance_provider"),
        ("GOVERNMENT", "government"),
    )
    address = models.CharField(max_length=128, null=True)
    billingAddress = models.CharField(max_length=128, null=True)
    accType = models.CharField(choices=USER_TYPES, max_length=20, default="customer")
    def __str__(self):
        return self.username

class Customer(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)
    dob = models.CharField(null=True)
    phoneNum = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Insurance_Provider(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)
    phoneNum = models.CharField(max_length=100)

class Law_Firm(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)
    phoneNum = models.CharField(max_length=100)

class Government(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)