Book Catalog

This Book Catalog application allows users to manage a collection of books, providing functionalities to add, view, and search for books within the catalog.

Files:
project.py:
Contains the core functionalities of the Book Catalog.
load_catalog(): Loads the book catalog from "catalog.json" or initializes an empty catalog.
save_catalog(catalog): Saves the current catalog data to "catalog.json".
add_book(catalog, title, author, genre, status, review): Adds a book with provided details to the catalog.
view_catalog(catalog): Displays the existing catalog of books.
search_books(catalog): Searches for books based on a keyword in the title, author, or genre.
Design Choices:
The book data is structured as a dictionary to encapsulate book details efficiently. Separate functions handle distinct functionalities, ensuring modularity and readability. JSON format is used for catalog storage due to its simplicity and ease of integration.

Testing:
test_project.py contains test cases for core functionalities:
test_add_book(): Tests the addition of a book to the catalog.
test_view_catalog(): Tests the viewing functionality of the catalog.
test_search_books(): Tests the search functionality in the catalog.
How to Run:
Ensure Python is installed. To run the application:

Open a terminal or command prompt.
Navigate to the project directory.
Run: python project.py.
Dependencies:
The project uses pytest for testing. Ensure it is installed before running tests.
