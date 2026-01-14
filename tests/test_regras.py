from src.mini_library.book import Book
from src.mini_library.user import User
from src.mini_library.leading import Leading


def test_leading():
    user = User("Anonymous", 5)

    book = Book("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "harry_potter_01")
    assert book.is_avaliable == True

    lend = Leading(book, user)
    assert book.is_avaliable == False

    lend.give_back()
    assert book.is_avaliable == True
