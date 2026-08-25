from django.forms.models import ModelForm
from book.models import Book, Category


class CrateBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "price", "pages", "author", "pub_date", "category"]


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
