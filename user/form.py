from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser


class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser

        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

        labels = {
            "username": "نام کاربری",
            "first_name": "نام",
            "last_name": "نام خانوادگی",
            "email": "ایمیل",
            "password1": "رمز عبور",
            "password2": "تکرار رمز عبور",
        }

        help_texts = {
            "username": "نام کاربری شما باید منحصر به فرد باشد.",
            "email": "یک ایمیل معتبر وارد کنید.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():

            field.widget.attrs.update(
                {
                    "class": "form-control",
                }
            )

            field.widget.attrs["placeholder"] = field.label

        # username
        self.fields["username"].widget.attrs.update(
            {
                "placeholder": "نام کاربری خود را وارد کنید",
                "autocomplete": "username",
            }
        )

        # first name
        self.fields["first_name"].widget.attrs.update(
            {
                "placeholder": "نام خود را وارد کنید",
            }
        )

        # last name
        self.fields["last_name"].widget.attrs.update(
            {
                "placeholder": "نام خانوادگی خود را وارد کنید",
            }
        )

        # email
        self.fields["email"].widget.attrs.update(
            {
                "placeholder": "example@gmail.com",
                "type": "email",
                "autocomplete": "email",
            }
        )

        # password
        self.fields["password1"].widget.attrs.update(
            {
                "placeholder": "رمز عبور خود را وارد کنید",
                "autocomplete": "new-password",
            }
        )

        # confirm password
        self.fields["password2"].widget.attrs.update(
            {
                "placeholder": "رمز عبور را دوباره وارد کنید",
                "autocomplete": "new-password",
            }
        )


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "نام کاربری خود را وارد کنید",
                "autocomplete": "username",
            }
        ),
    )

    password = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "رمز عبور خود را وارد کنید",
                "autocomplete": "current-password",
            }
        ),
    )
