from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control mb-4",
            "class": "u-full-width",
            "placeholder": "Username",
        })
        self.fields["first_name"].widget.attrs.update({
            "class": "form-control mb-4",
            "class": "u-full-width",
            "placeholder": "First Name",
        })
        self.fields["last_name"].widget.attrs.update({
            "class": "form-control mb-4",
            "class": "u-full-width",
            "placeholder": "Last Name",
        })
        self.fields["email"].widget.attrs.update({
            "class": "form-control mb-4",
            "class": "u-full-width",
            "placeholder": "E-mail",
        })
        self.fields["password1"].widget.attrs.update({
            "class": "form-control mb-4",
            "class": "u-full-width",
            "placeholder": "Password",
        })
        self.fields["password2"].widget.attrs.update({
            "class": "form-control mb-4",
            "class": "u-full-width",
            "placeholder": "Confirm Password",
        })
    username = forms.CharField(max_length=64)
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField(max_length=64)
    password1 = forms.CharField(max_length=64,
                                widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=64,
                                widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control mb-4 mr-4",
            "class": "u-full-width",
            "placeholder": "Username"
        })
        # needed to do this otherwise the maxlength of username was 150
        self.fields["username"].widget.attrs["maxlength"] = 64

        self.fields["password"].widget.attrs.update({
            "class": "form-control mb-4 mr-4",
            "class": "u-full-width",
            "placeholder": "Password"
        })

    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64,
                               widget=forms.PasswordInput())

    class Meta:
        fields = [
            "username",
            "password",
        ]
