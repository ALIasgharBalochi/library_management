from django.urls import path, include
from book.views import (
    BookList,
    BookDetail,
    CreateBookView,
    BookSearch,
    DeleteBookView,
    UpdateBookView,
    BookFiltering,
    CreateCategoryView,
    delete_book_by_filtring,
    home,
)

urlpatterns = [
    path("", home, name="home"),
    path("book_list/", BookList.as_view(), name="book_list"),
    path("book_detail/<int:pk>/", BookDetail.as_view(), name="book_detail"),
    path("create_book/", CreateBookView.as_view(), name="create_book"),
    path("update_book/<int:pk>", UpdateBookView.as_view(), name="update_book"),
    path("delete_book/<int:pk>", DeleteBookView.as_view(), name="delete_book"),
    path("search/", BookSearch.as_view(), name="search"),
    path("filter/", BookFiltering.as_view(), name="filter"),
    path("create_category/", CreateCategoryView.as_view(), name="create_category"),
    path(
        "delete_book_by_filter/", delete_book_by_filtring, name="delete_books_filtering"
    ),
]
