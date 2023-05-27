from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class SignUpPageView(UserCreationForm):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
