from django.urls import path
from .views import RegisterUser, LoginView, UserFaveBooks, add_to_favarit

urlpatterns = [
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("fav_book/<int:userid>/", UserFaveBooks.as_view(), name="user_fav_books"),
    path(
        "add_fav_book/<int:userid>/<int:bookid>/",
        add_to_favarit,
        name="add_fav_books",
    ),
]
