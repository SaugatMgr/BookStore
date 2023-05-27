from django.urls import path

from .views import (
    HomePageView,
    BookDetailView,
    AboutPageView,
    ContactPageView,
    NewsLetterView,
    ReviewView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="detail"),
    path("books/about/", AboutPageView.as_view(), name="about"),
    path("books/contact/", ContactPageView.as_view(), name="contact"),
    path("books/newsletter/", NewsLetterView.as_view(), name="newsletter"),
    path("books/review/", ReviewView.as_view(), name="review"),
]
