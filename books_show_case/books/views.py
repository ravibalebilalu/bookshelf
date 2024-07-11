from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from books.models import Book
from datetime import datetime
from collections import defaultdict


def index(request):
    book = Book.objects.all()
    context = {
        "book":book
    }
    template = loader.get_template("books/home.html")
    return HttpResponse(template.render(context,request))

def authors(request):
    books = Book.objects.all().order_by('bookauthors')
    author_books = defaultdict(set)  # Using a set to avoid duplicates

    for book in books:
        authors_list = book.bookauthors.split('/')  # Assuming authors are separated by '/'
        for author in authors_list:
            author_books[author.strip()].add(book.booktitle)
    
    context = {
        "authors": [{"bookauthors": author, "booktitles": list(titles)} for author, titles in author_books.items()]
    }
    return render(request, "books/authors.html", context)

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
