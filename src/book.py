class Book:
    """
    Represents a book in the library.
    """

    def __init__(self, isbn: str, title: str, author: str, copies: int):
        """
        Initialize a Book object.

        :param isbn: Unique ISBN of the book
        :param title: Title of the book
        :param author: Author name
        :param copies: Number of available copies
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        """
        String representation of the book.
        """
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, Copies: {self.copies})"
