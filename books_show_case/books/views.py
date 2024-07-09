from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from books.models import Book
from datetime import datetime

def index(request):
    book = Book.objects.all()[:20]

    context={
        "book":book
    }
    template = loader.get_template("books/home.html")
    return HttpResponse(template.render(context,request))

def authors(request):
    template = loader.get_template("books/authors.html")
    authors = Book.objects.values('bookauthors').distinct().order_by("bookauthors")
    



    
    context = {
        "authors":authors
    }
    return HttpResponse(template.render(context,request))

"""
    bookid booktitle bookauthors bookrating bookisbn bookisbn13 book_language_code bookpages book_rating_counts 
    book_text_reviews_count book_publication_date book_publisher 
    """

def filters(request):
    template = loader.get_template("books/filters.html")

    
    all_entries = Book.objects.all()
     
     
    context = {
         "entries": all_entries
    }
    return HttpResponse(template.render(context, request))
