import os
import csv
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_show_case.settings')
django.setup()

print("Shrekrishna................")

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%m/%d/%Y").date()
    except ValueError:
        return None  # Handle invalid dates

def data_from_csv(file_path):
    from books.models import Book
    with open(file_path, "r") as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            publication_date = parse_date(row["publication_date"])
            if publication_date is None:
                print(f"Invalid date format for book {row['title']}: {row['publication_date']}")
                continue

            book_details = Book(
                bookid=row["bookID"],
                booktitle=row["title"],
                bookauthors=row["authors"],
                bookrating=row["average_rating"],
                bookisbn=row["isbn"],
                bookisbn13=row["isbn13"],
                book_language_code=row["language_code"],
                bookpages=row["num_pages"],
                book_rating_counts=row["ratings_count"],
                book_text_reviews_count=row["text_reviews_count"],
                book_publication_date=publication_date,
                book_publisher=row["publisher"]
            )

            book_details.save()
            print(f"Saving {row['title']}....")

file_path = "../data/books.csv"
data_from_csv(file_path)
