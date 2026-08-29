from django.shortcuts import render
from book.models import Book, Category
from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from book.form import CrateBookForm, CategoryForm
from book.service import BookService
from user.service import UserService

# Create your views here.


def home(request):
    return render(request, "book/home.html")


class BookList(ListView):
    model = Book
    template_name = "book/list_books.html"
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categorys"] = Category.objects.all()
        user = self.request.user
        if user.is_authenticated:
            context["favorite_book_ids"] = UserService.get_fave_book(user.id)

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
    template_name = "book/delete_book.html"
    context_object_name = "object"
    success_url = reverse_lazy("book_list")


def delete_book_by_filtring(request):
    pub_date = request.GET.get("pub_date")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    category = request.GET.get("category")

    if pub_date or min_price or max_price or category:

        books = BookService.filtering(pub_date, min_price, max_price, category)

        count = books.count()
        books.delete()

        return render(
            request,
            "book/delete_success.html",
            {
                "count": count,
            },
        )

    return render(
        request,
        "book/delete_success.html",
        {
            "error": True,
        },
    )


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
        user = self.request.user
        if user.is_authenticated:
            context["favorite_book_ids"] = UserService.get_fave_book(user.id)

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
        user = self.request.user
        if user.is_authenticated:
            context["favorite_book_ids"] = UserService.get_fave_book(user.id)

        return context


# category
class CreateCategoryView(FormView):
    form_class = CategoryForm
    template_name = "book/create_category.html"
    success_url = reverse_lazy("book_list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
