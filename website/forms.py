from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="")
    first_name = forms.CharField(label="", max_length=50)
    last_name = forms.CharField(label="", max_length=50)

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
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["password1"].label = ""
        self.fields["password1"].help_text = (
            "<ul class='password1_help'><li>Password must not match other personal info.</li><li>Password must contains at least 8 characters.</li><li>Password must contains at least a capital letter, a small letter, a number, a symbole.</li></ul>"
        )

        self.fields["password2"].label = ""
        self.fields["password2"].help_text = (
            "<span class='password2_help'>Enter same password as before</span>"
        )
