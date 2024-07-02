from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from books.models import Book

def index(request):
    book = Book.objects.all()

    context={
        "book":book
    }
    template = loader.get_template("books/home.html")
    return HttpResponse(template.render(context,request))
