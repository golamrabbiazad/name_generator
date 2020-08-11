from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(req):
    return render(req, "app/index.html")


def greet(req, name):
    return render(req, "app/greet.html", {
        "name": name.capitalize()
    })
