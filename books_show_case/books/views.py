from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from books.models import Book

def index(request):
    book = Book.objects.all()[:20]

    context={
        "book":book
    }
    template = loader.get_template("books/home.html")
    return HttpResponse(template.render(context,request))

def authors(request):
    books = Book.objects.values('bookauthors').distinct().order_by("bookauthors")
    template = loader.get_template("books/authors.html")
    context = {
        "books":books
    }
    return HttpResponse(template.render(context,request))