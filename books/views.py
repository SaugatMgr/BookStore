from django.shortcuts import redirect, render
from django.views.generic import View, ListView, DetailView, TemplateView
from django.contrib import messages
from django.http import JsonResponse

from .forms import ContactForm, NewsLetterForm

from .models import Book, Genre


class HomePageView(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filter_object = Book.objects.filter(
            copies_sold__gt=0).order_by("-copies_sold")

        context['best_selling_book'] = filter_object.first()

        context['popular_books_top'] = filter_object[:4]

        context['popular_books_bottom'] = filter_object[4:7]

        context['billboard_books'] = Book.objects.all()[:3:-1]

        context['featured_books'] = filter_object[:4:-1]

        context['genres'] = Genre.objects.all()[:5]

        return context

# class BookByGenre(ListView):
#     model = Book
#     template_name = "booksaw/main/popular_books/books_by_genre/popular_books_by_genre.html"
#     context_object_name = "books_by_genre"

#     def get_queryset(self):
#         query = super().get_queryset()

#         query = query.filter(
#             copies_sold__gt=0,
#             genre = self.kwargs['genre_id'],
#         )
#         return query


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(View):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, "Your message has been successfully sent—thank you for reaching out to us!"
            )
            return redirect("contact")
        else:
            messages.error(
                request, "Please ensure all required fields are filled out correctly \
                to submit the contact form."
            )
            return render(request, self.template_name, {"form": form})


class BookDetailView(DetailView):
    model = Book
    template_name = 'booksaw/main/detail/book_detail.html'
    context_object_name = 'book'


class NewsLetterView(View):
    def post(self, request, *args, **kwargs):
        ajax_format = request.headers.get("x-requested-with")
        
        if ajax_format == "XMLHttpRequest":
            form = NewsLetterForm(request.POST)
            if form.is_valid():
                form.save()
                
                return JsonResponse(
                    {
                    "success": True,
                    "message": "Thank you for subscribing to our newsletter! We look forward to \
                                sharing exciting literary adventures with you straight to your inbox."
                    },
                    status=201, # create code
                )
            else:
                return JsonResponse(
                    {
                    "success": False,
                    "message": "Oops! It seems there was an issue with your newsletter \
                                subscription—please double-check your email and try again."
                    },
                    status=400,
                )
        return JsonResponse(
            {
                'success': False,
                'message': 'Cannot process.Must be and AJAX XMLHttpRequest.',
            },
            status=400,
        )