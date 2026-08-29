from django.forms.models import ModelForm
from book.models import Book, Category
from django import forms


class CrateBookForm(ModelForm):

    class Meta:
        model = Book

        fields = [
            "title",
            "price",
            "pages",
            "author",
            "pub_date",
            "category",
        ]

        widgets = {
            "pub_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "w-full rounded-2xl border border-black/10 bg-white px-5 py-4 text-sm font-medium outline-none transition focus:border-black focus:ring-4 focus:ring-black/5",
                }
            ),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        input_class = (
            "w-full "
            "rounded-2xl "
            "border border-black/10 "
            "bg-white "
            "px-5 py-4 "
            "text-sm font-medium "
            "outline-none "
            "transition "
            "placeholder:text-black/30 "
            "hover:border-black/20 "
            "focus:border-black "
            "focus:ring-4 "
            "focus:ring-black/5"
        )

        select_class = (
            "w-full "
            "rounded-2xl "
            "border border-black/10 "
            "bg-white "
            "px-5 py-4 "
            "text-sm font-medium "
            "outline-none "
            "transition "
            "hover:border-black/20 "
            "focus:border-black "
            "focus:ring-4 "
            "focus:ring-black/5"
        )

        for name, field in self.fields.items():

            if name != "pub_date":
                field.widget.attrs.update(
                    {
                        "class": input_class,
                    }
                )

        self.fields["category"].widget.attrs.update(
            {
                "class": select_class,
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
