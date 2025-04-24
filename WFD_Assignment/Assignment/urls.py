"""
URL configuration for WFD_Assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("login", views.login_page, name="login"),
    path("logout", views.logout_page, name="logout"),
    path("register", views.register, name="register"),
    path("register_customer", views.registerCustomer, name="registerCustomer"),
    path("register_insurance_provider", views.registerInsuranceProvider, name="registerInsuranceProvider"),
    path("register_law_firm", views.registerLawFirm, name="registerLawFirm"),
    path("register_government", views.registerGovernment, name="registerGovernment"),
    path("account", views.account, name="account"),
    path("get_insurance", views.get_insurance, name="getInsurance"),
    path("view_insurance", views.view_insurance, name="viewInsurance"),
    path("sell_insurance", views.sell_insurance, name="sellInsurance"),
    path("home", views.home, name="home"),
]
