from .book import Book
from .user import User
from .leading import Leading


def main():
    user = User("Anonymous", 5)

    book = Book("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "harry_potter_01")
    print(f"O livro está disponível? {book.is_avaliable}")

    lend = Leading(book, user)
    print(f"O livro está disponível? {book.is_avaliable}")

    lend.give_back()
    print(f"O livro está disponível? {book.is_avaliable}")


if __name__ == "__main__":
    main()
