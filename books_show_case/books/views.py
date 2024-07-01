from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    name = ["Shreekrishna","Narahari","Madhusudhana","Jayarama","Chanuramardhana"]
    context={
        "name": name
    }
    template = loader.get_template("books/home.html")
    return HttpResponse(template.render(context,request))
