import pytest
from book import Book

@pytest.mark.parametrize("title, isbn", [
    ("Watchmen", "978-1779501127"),
    ("1984", "978-0451524935"),
    ("To Kill a Mockingbird", "978-0060935467"),
])
def test_valid_creation(title, isbn):
    book = Book(title, isbn)
    assert book.title == title
    assert book.isbn == isbn

@pytest.mark.parametrize("title, isbn", [
    ("", "978-1779501127"),
])
def test_creation_with_invalid_title(title, isbn):
    with pytest.raises(RuntimeError, match="Title must not be empty"):
        Book(title, isbn)

@pytest.mark.parametrize("title, isbn", [
    ("Watchmen", "978-1779501128"),  # Invalid checksum
    ("1984", "978-045152493"),       # Less than 13 digits
    ("To Kill a Mockingbird", "978-00609354670"),  # More than 13 digits
    ("To Kill a Mockingbird", "978-006093546X"),   # Invalid character
])
def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError, match="Invalid ISBN number"):
        Book(title, isbn)

