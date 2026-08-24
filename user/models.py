from django.db import models
from django.contrib.auth.models import AbstractUser
from book.models import Book

# Create your models here.


class CustomUser(AbstractUser):
    fave_books = models.ManyToManyField(Book)
