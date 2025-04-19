from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, "assignment/index.html")
def register(request):
    return render(request, "assignment/register.html")
def home(request):
    return render(request, "assignment/home.html")