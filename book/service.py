from book.models import Book, Author


class BookService:

    @classmethod
    def get_book(book_id: int):
        book = Book.objects.filter(id=id)
        return book
