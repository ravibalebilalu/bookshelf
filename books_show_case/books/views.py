from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from books.models import Book
from datetime import datetime
from collections import defaultdict
from django.urls import reverse


def index(request):
    book = Book.objects.all()[:100]
    context = {
        "book":book
    }
    template = loader.get_template("books/home.html")
    return HttpResponse(template.render(context,request))

def authors(request):
    books = Book.objects.all().order_by('bookauthors')
    author_books = defaultdict(list)  

    for book in books:
        authors_list = book.bookauthors.split('/')   
        for author in authors_list:
            author_books[author.strip()].append({"title":book.booktitle,"url":reverse("book_details",args=[book.id])})
    
    context = {
        "authors": [{"bookauthors": author, "booktitles": titles} for author, titles in author_books.items()]
    }
    return render(request, "books/authors.html", context)

"""
    bookid booktitle bookauthors bookrating bookisbn bookisbn13 book_language_code bookpages book_rating_counts 
    book_text_reviews_count book_publication_date book_publisher 
    """


def book_details(request,book_id):
    print("shreekrishna")
    book = Book.objects.get(id=book_id)
    print(book)
    context = {"book":book}

    template = loader.get_template("books/book_details.html")

    return HttpResponse(template.render(context,request))







def filters(request):
    template = loader.get_template("books/filters.html")

    
    all_entries = Book.objects.all()
     
     
    context = {
         "entries": all_entries
    }
    return HttpResponse(template.render(context, request))
