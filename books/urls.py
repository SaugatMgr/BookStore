from django.urls import path

from .views import (
    HomePageView,
    BookDetailView,
    AboutPageView,
    ContactPageView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="detail"),
    path("books/about/", AboutPageView.as_view(), name="about"),
    path("books/contact/", ContactPageView.as_view(), name="contact"),
]
