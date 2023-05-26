from django.urls import path

from .views import (
    HomePageView,
    BookDetailView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="detail"),
]
