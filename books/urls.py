from django.urls import path

from .views import (
    HomePageView,
    BookDetailView,
    AboutPageView,
    ContactPageView,
    NewsLetterView,
    ReviewView,
    BooksByAuthorView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("books/detail/<slug:slug>/", BookDetailView.as_view(), name="book_detail"),
    path("books/about/", AboutPageView.as_view(), name="about"),
    path("books/contact/", ContactPageView.as_view(), name="contact"),
    path("books/newsletter/", NewsLetterView.as_view(), name="newsletter"),
    path("books/review/", ReviewView.as_view(), name="review"),
    path("books/<str:author_name>/", BooksByAuthorView.as_view(), name="author_books"),
]
