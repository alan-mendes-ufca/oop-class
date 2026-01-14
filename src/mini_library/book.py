class Book:
    def __init__(
        self, title: str, author: str, identificator: str, is_avaliable: bool = True
    ):
        self.title = title
        self.author = author
        self.identificator = identificator
        self.is_avaliable = is_avaliable
