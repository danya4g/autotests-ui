import pytest

@pytest.fixture
def clear_book_database() -> None:
    print("clearing book database")

@pytest.fixture
def fill_book_database() -> None:
    print("filling book database")

@pytest.mark.usefixtures("clear_book_database")
def test_read_all_books_in_library(clear_book_database, fill_book_database):
    print("reading all books in library")

@pytest.mark.usefixtures("clearing book database", "fill_book_database")

class TestReadAllBooksInLibrary:
    def test_read_all_books_in_library(self):
        pass

    def test_delete_all_books_in_library(self):
        pass