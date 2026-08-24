from django.shortcuts import render
from book.models import Book
from django.views.generic import ListView, DetailView

# Create your views here.


class BookList(ListView):
    model = Book
    template_name = "book/list_books.html"
    context_object_name = "books"


class BookDetail(DetailView):
    model = Book
    template_name = "book/book_details.html"
    context_object_name = "book"
