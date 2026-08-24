from django.shortcuts import render
from book.models import Book
from django.views.generic import ListView

# Create your views here.


class BookList(ListView):
    model = Book
    template_name = "book/list_books.html"
    context_object_name = "books"
