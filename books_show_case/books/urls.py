from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="index"),
    path("authors/",views.authors,name="authors"),
    path("filters/",views.filters,name="filters"),
    path("book/<int:book_id>/",views.book_details,name="book_details"),
    
]
