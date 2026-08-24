from django.forms.models import ModelForm
from book.models import Book


class CrateBook(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "price", "pages", "author", "pub_date", "category"]
