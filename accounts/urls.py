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
    # Signup
    path("signup/", SignUpPageView.as_view(), name="signup"),
    # Login/Logout
    path("login/", auth_views.LoginView.as_view(
        template_name="registration/login.html",
        authentication_form=LoginForm),
        name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # Password Change
    path("password-change/", auth_views.PasswordChangeView.as_view(
        form_class=ChangePasswordForm),
        name="password_change"),
    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),
    # Password Reset
    path("password-reset/", auth_views.PasswordResetView.as_view(),
         name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path("password-reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path("password-reset/complete/", auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
]
