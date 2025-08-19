from random import randint
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={
                "class": "form-input",
                "id": "id_email",
                "placeholder": "Email",
                "autocomplete": "off",
                "required": True,
            }
        ),
    )

    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "id": "id_first_name",
                "placeholder": "First Name",
                "autocomplete": "off",
                "required": True,
            }
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "id": "id_last_name",
                "placeholder": "Last Name",
                "autocomplete": "off",
                "required": True,
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["password1"].label = ""
        self.fields["password1"].help_text = (
            "<ul class='password1_help'><li>Password must not match other personal info.</li><li>Password must contains at least 8 characters.</li><li>Password must contains at least a capital letter, a small letter, a number, a symbole.</li></ul>"
        )
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "class": "form-input",
                "id": "id_password1",
                "placeholder": "Password",
                "autocomplete": "new-password",
                "required": True,
            }
        )

        self.fields["password2"].label = ""
        self.fields["password2"].help_text = (
            "<span class='password2_help'>Enter same password as before</span>"
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "class": "form-input",
                "id": "id_password2",
                "placeholder": "Confirm Password",
                "autocomplete": "new-password",
                "required": True,
            }
        )

    def save(self, commit=True):
        self.instance.username = (
            self.data["email"].split("@")[0] + f"{randint(1000, 9999)}"
        )
        return super().save(commit)
