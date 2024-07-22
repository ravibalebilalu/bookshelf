# Bookshelf Project

## Overview

The Bookshelf Project is a web application built using Django that allows users to manage and browse a collection of books. Users can filter books based on various criteria such as title, rating, number of pages, and language.

## Features

-   View a collection of books.
-   Filter books by title, rating, number of pages, and language.
-   Pagination for easy navigation through the book collection.

## Installation

### Prerequisites

-   Python 3.x
-   Django
-   Virtualenv (recommended)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/ravibalebilalu/bookshelf.git
    cd bookshelf
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

5. Run dta updater script:

    `python data_update.py`

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application at `http://127.0.0.1:8000/`.

## Usage

#

### Filtering Books

-   Use the filter buttons on the main page to filter books by title, rating, number of pages, and language.

## Project Structure

-   `books/`: Contains the main application code.
-   `books/templates/`: HTML templates for the application.
-   `books/static/`: Static files (CSS, JavaScript, images).
-   `books/models.py`: Database models for the application.
-   `books/views.py`: View functions for handling HTTP requests.
-   `books/urls.py`: URL routing for the application.
-   `manage.py`: Django management script.

## Contributing

If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the Apache License 2.0.

## Acknowledgments

-   Thanks to the Django community for their support and excellent documentation.
