import pytest
from project import load_catalog, save_catalog, add_book, view_catalog, search_books
from unittest.mock import patch

def test_add_book():
    catalog = {"books": []}
    add_book(catalog, "Test Title", "Test Author", "Test Genre", "read", "Test Review")
    assert len(catalog["books"]) == 1



def test_view_catalog(capsys):
    catalog = {"books": [{"title": "Test Book", "author": "Test Author", "status": "read"}]}
    view_catalog(catalog)
    captured = capsys.readouterr()
    assert "1. Test Book by Test Author (read)" in captured.out



# Your other test functions...

def test_search_books(capsys):
    catalog = {"books": [{"title": "Python Book", "author": "Test Author", "status": "read"}]}

    # Mocking the input function to provide a keyword
    with patch('builtins.input', return_value='python'):
        search_books(catalog)

    captured = capsys.readouterr()
    assert "Python Book by Test Author (read)" in captured.out


