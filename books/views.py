from django.shortcuts import render
from django.views.generic import ListView

from .models import Book, Genre


class HomePageView(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filter_object = Book.objects.filter(copies_sold__gt=0).order_by("-copies_sold")
        
        context['best_selling_book'] = filter_object.first()

        context['popular_books_top'] = filter_object[:4]
                                                    
        context['popular_books_bottom'] = filter_object[4:7]
        
        context['genres'] = Genre.objects.all()[:5]
                                                    
        return context
    
# class BookByGenre(ListView):
#     model = Book
#     template_name = "booksaw/main/popular books/popular_books.html"
#     context_object_name = "books_by_genre"
    
#     def get_queryset(self):
#         query = super().get_queryset()
        
#         query = query.filter(
#             copies_sold__gt=0,
#             genre = self.kwargs['genre_id'],
#         )
#         return query
