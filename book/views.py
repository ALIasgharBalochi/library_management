from django.shortcuts import render
from book.models import Book
from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from book.form import CrateBookForm
from book.service import BookService

# Create your views here.


class BookList(ListView):
    model = Book
    template_name = "book/list_books.html"
    context_object_name = "books"


class BookDetail(DetailView):
    model = Book
    template_name = "book/book_details.html"
    context_object_name = "book"


class CreateBookView(FormView):
    form_class = CrateBookForm
    template_name = "book/create_book.html"
    success_url = reverse_lazy("book_list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateBookView(UpdateView):
    model = Book
    form_class = CrateBookForm
    template_name = "book/update_book.html"
    success_url = reverse_lazy("book_list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteBookView(DeleteView):
    model = Book
    # form_class = CrateBookForm
    template_name = "book/delete_book.html"
    context_object_name = "object"
    success_url = reverse_lazy("book_list")


class BookSearch(ListView):
    template_name = "book/list_books.html"
    context_object_name = "books"

    def get_queryset(self):
        q = self.request.GET.get("q")

        if q:
            books = BookService.search(q)
            return books
