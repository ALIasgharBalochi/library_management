from django.urls import path, include
from book.views import (
    BookList,
    BookDetail,
    CreateBookView,
    BookSearch,
    DeleteBookView,
    UpdateBookView,
)

urlpatterns = [
    path("book_list/", BookList.as_view(), name="book_list"),
    path("book_detail/<int:pk>/", BookDetail.as_view(), name="book_detail"),
    path("create_book/", CreateBookView.as_view(), name="create_book"),
    path("update_book/<int:pk>", UpdateBookView.as_view(), name="update_book"),
    path("delete_book/<int:pk>", DeleteBookView.as_view(), name="delete_book"),
    path("search/", BookSearch.as_view(), name="search"),
]
