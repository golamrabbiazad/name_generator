from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
# Create your views here.

tasks = []


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def index(req):
    if "tasks" not in req.session:
        req.session["tasks"] = []
    return render(req, "tasks/index.html", {
        "tasks": req.session["tasks"]
    })


def add(req):
    if req.method == "POST":
        form = NewTaskForm(req.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            req.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(req, "tasks/add.html", {
                "form": form
            })
    return render(req, "tasks/add.html", {
        "form": NewTaskForm()
    })
