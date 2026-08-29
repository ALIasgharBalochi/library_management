from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import FormView, ListView
from .form import RegisterForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from .service import UserService
from book.views import BookListBase

# Create your views here.


class RegisterUser(FormView):
    form_class = RegisterForm
    template_name = "user/register.html"
    success_url = reverse_lazy("book_list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print("formet moshkel dare aghaaaaaaaaa")
        print(form.errors)
        return super().form_invalid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name = "user/login.html"
    success_url = reverse_lazy("book_list")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def form_invalid(self, form):
        print("formet moshkel dare aghaaaaaaaaa")
        print(form.errors)
        return super().form_invalid(form)


class UserFaveBooks(BookListBase):
    def get_queryset(self):
        userid = int(self.kwargs["userid"])
        books = UserService.get_fave_book(userid)
        if books:
            return books


def add_to_favarit(request, userid, bookid):
    res = UserService.add_to_fave_book(userid, bookid)

    return render(
        request,
        "user/favorit_success.html",
        {
            "bookid": bookid,
        },
    )


def profile(request):
    return render(request, "user/profile.html")
