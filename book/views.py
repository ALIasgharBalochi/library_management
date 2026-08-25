from django.shortcuts import render
from book.models import Book, Category
from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from book.form import CrateBookForm, CategoryForm
from book.service import BookService

# Create your views here.


class BookList(ListView):
    model = Book
    template_name = "book/list_books.html"
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categorys"] = Category.objects.all()

        return context


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


class BookFiltering(ListView):
    template_name = "book/list_books.html"
    context_object_name = "books"

    def get_queryset(self):
        pub_date = self.request.GET.get("pub_date")
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")
        category = self.request.GET.get("category")

        if pub_date or min_price or max_price or category:
            books = BookService.filtering(pub_date, min_price, max_price, category)
            return books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categorys"] = Category.objects.all()

        return context


class BookSearch(ListView):
    template_name = "book/list_books.html"
    context_object_name = "books"

    def get_queryset(self):
        q = self.request.GET.get("q")

        if q:
            books = BookService.search(q)
            return books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categorys"] = Category.objects.all()

        return context


# category
class CreateCategoryView(FormView):
    form_class = CategoryForm
    template_name = "book/create_category.html"
    success_url = reverse_lazy("book_list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
