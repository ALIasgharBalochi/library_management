from django.urls import path, include
from book.views import BookList

urlpatterns = [path("book_list/", BookList.as_view(), name="book_list")]
