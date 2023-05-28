from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import (
    LoginForm,
    ChangePasswordForm,
)

from .views import (
    SignUpPageView,
)

urlpatterns = [
    path("signup/", SignUpPageView.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(
        template_name="registration/login.html",
        authentication_form=LoginForm),
        name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("password-change/", auth_views.PasswordChangeView.as_view(
        form_class=ChangePasswordForm),
        name="password_change"),
    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),
]
