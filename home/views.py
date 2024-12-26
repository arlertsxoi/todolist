from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
tasks = ["meow","kk","oo"]

def index (request):
    return render (request, "home/home.html", {
        "tasks" : tasks 
    })

def add (request):
    return render (request, "home/home.html", {
       
    })