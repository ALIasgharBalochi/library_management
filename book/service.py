from book.models import Book, Author
from django.db.models import Q


class BookService:

    @staticmethod
    def search(q):
        books = Book.objects.filter(
            Q(title__icontains=q) | Q(author__name__icontains=q)
        )
        return books
