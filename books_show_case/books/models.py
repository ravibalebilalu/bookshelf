from django.db import models

 #'bookID', 'title', 'authors', 'average_rating', 'isbn', 'isbn13', 'language_code', 'num_pages', 'ratings_count', 'text_reviews_count', 'publication_date', 'publisher'

"""
bookID                  int64,
title                  object,
authors                object,
average_rating        float64,
isbn                   object,
isbn13                  int64,
language_code          object,
num_pages               int64,
ratings_count           int64,
text_reviews_count      int64,
publication_date       object
publisher              object
"""

"""
title------- 254
authors------- 750
isbn------- 10
language_code------- 5
publication_date------- 10
publisher------- 67
"""
class Book(models.Model):
    bookid = models.IntegerField()
    booktitle = models.CharField(max_length=300)
    bookauthors = models.CharField(max_length=800)
    bookrating = models.FloatField()
    bookisbn = models.CharField(max_length=10)
    bookisbn13 = models.IntegerField()
    book_language_code = models.CharField(max_length=5)
    bookpages = models.IntegerField()
    book_rating_counts = models.IntegerField()
    book_text_reviews_count = models.IntegerField()
    book_publication_date = models.DateField()
    book_publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.booktitle



 
