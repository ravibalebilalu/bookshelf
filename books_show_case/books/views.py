from django.shortcuts import render,get_object_or_404,redirect
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

    lang = ['eng', 'en-US', 'fre', 'spa', 'en-GB', 'mul', 'grc', 'enm','en-CA', 'ger', 'jpn', 'ara', 'nl', 'zho', 'lat', 'por', 'srp','ita', 'rus', 'msa', 'glg', 'wel', 'swe', 'nor', 'tur', 'gla','ale']
    lang_dict = {
    'eng': 'English',
    'en-US': 'English (US)',
    'fre': 'French',
    'spa': 'Spanish',
    'en-GB': 'English (UK)',
    'mul': 'Multiple languages',
    'grc': 'Ancient Greek',
    'enm': 'Middle English',
    'en-CA': 'English (Canada)',
    'ger': 'German',
    'jpn': 'Japanese',
    'ara': 'Arabic',
    'nl': 'Dutch',
    'zho': 'Chinese',
    'lat': 'Latin',
    'por': 'Portuguese',
    'srp': 'Serbian',
    'ita': 'Italian',
    'rus': 'Russian',
    'msa': 'Malay',
    'glg': 'Galician',
    'wel': 'Welsh',
    'swe': 'Swedish',
    'nor': 'Norwegian',
    'tur': 'Turkish',
    'gla': 'Scottish Gaelic',
    'ale': 'Aleut'
}

    flag=""
    all_entries = Book.objects.all()
    filter_by = request.GET.get("filter")
    selected_language = request.GET.get("language")
    print(selected_language)
    
    if filter_by == "alphabatic":
        all_entries = all_entries.order_by("booktitle")
         
    elif filter_by == "ratingh2l":
        all_entries = all_entries.order_by("-bookrating")
        flag="rating"
    elif filter_by == "rating-l2h":
        all_entries = all_entries.order_by("bookrating")
        flag="rating"
    elif filter_by == "numberOfPagesl2h":
        all_entries = all_entries.order_by("bookpages")
        flag="pages"
    elif filter_by == "numberOfPagesh2l":
        all_entries = all_entries.order_by("-bookpages")
        flag="pages"
     
    if selected_language:
        all_entries = all_entries.filter(book_language_code=selected_language)
     
    context = {
         "entries": all_entries,
         "flag":flag,
         "lang":lang,
         "lang_dict":lang_dict
    }
    return HttpResponse(template.render(context, request))




 