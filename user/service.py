from .models import CustomUser
from book.models import Book


class UserService:

    @staticmethod
    def get_fave_book(userid):
        user = CustomUser.objects.get(id=userid)
        return user.fave_books.all()

    @staticmethod
    def add_to_fave_book(userid, bookid):
        user = CustomUser.objects.get(id=userid)
        book = Book.objects.get(id=bookid)
        user.fave_books.add(book)
        user.save()
        return user
