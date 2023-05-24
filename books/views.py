from django.shortcuts import render
from django.views.generic import ListView

from .models import Book


class HomePageView(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = "books"
