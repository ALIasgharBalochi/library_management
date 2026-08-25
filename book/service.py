from book.models import Book, Author
from django.db.models import Q


class BookService:

    @staticmethod
    def search(q):
        books = Book.objects.filter(
            Q(title__icontains=q) | Q(author__name__icontains=q)
        )
        return books

    @staticmethod
    def filtering(pub_date, min_p, max_p, category):
        books = Book.objects.all()

        if pub_date:
            books = books.filter(pub_date=pub_date)
        if min_p:
            books = books.filter(price__gte=min_p)
        if max_p:
            books = books.filter(price__lte=max_p)
        if category:
            books = books.filter(category=category)

        return books
