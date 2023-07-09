from django.urls import path

from .views import (
    HomePageView,
    BookDetailView,
    AboutPageView,
    ContactPageView,
    NewsLetterView,
    ReviewView,
    BooksByAuthorView,
    AddBookView,
    AllBooksView,
    UpdateBookView,
    DeleteBookView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("books/add-book/", AddBookView.as_view(), name="add_book"),
    path("books/all-books/", AllBooksView.as_view(), name="all_books"),
    path("books/update-book/<slug:slug>/", UpdateBookView.as_view(), name="update_book"),
    path("books/delete-book/<slug:slug>/", DeleteBookView.as_view(), name="delete_book"),
    path("books/detail/<slug:slug>/", BookDetailView.as_view(), name="book_detail"),
    path("books/about/", AboutPageView.as_view(), name="about"),
    path("books/contact/", ContactPageView.as_view(), name="contact"),
    path("books/newsletter/", NewsLetterView.as_view(), name="newsletter"),
    path("books/review/", ReviewView.as_view(), name="review"),
    path("books/<str:author_name>/", BooksByAuthorView.as_view(), name="author_books"),
]
