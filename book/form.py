from django.forms.models import ModelForm
from book.models import Book, Category


class CrateBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "price", "pages", "author", "pub_date", "category"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    "class": "form-control",
                }
            )

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-select",
            }
        )


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "نام دسته‌بندی را وارد کنید",
            }
        )
