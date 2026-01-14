from src.mini_library.book import Book
from src.mini_library.user import User
from src.mini_library.leading import Leading


def test_instance_book():
    b = Book("teste", "teste", "teste")
    assert isinstance(b, Book) == True


def test_instance_user():
    u = User("teste", 5)
    assert isinstance(u, User) == True


def test_instance_leading():
    u = User("teste", 5)
    b = Book("teste", "teste", "teste")
    l = Leading(b, u)
    assert isinstance(l, Leading) == True
