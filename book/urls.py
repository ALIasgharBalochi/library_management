from django.urls import path, include
from book.views import BookList, BookDetail

urlpatterns = [
    path("book_list/", BookList.as_view(), name="book_list"),
    path("book_detail/<int:pk>/", BookDetail.as_view(), name="book_detail"),
]
