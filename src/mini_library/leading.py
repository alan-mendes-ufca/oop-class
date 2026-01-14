from .book import Book
from .user import User


class Leading:
    def __init__(self, book: Book, user: User, is_active: bool = True):
        self.book = book
        self.user = user
        self.is_active = is_active

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool):
        if not self.book.is_avaliable:
            raise ValueError("O livro já está emprestado. Solicitação rejeitada.")
        self.book.is_avaliable = not value
        self._is_active = value

    def give_back(self):
        self.book.is_avaliable = True
        self.is_active = False
