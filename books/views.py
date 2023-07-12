from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    View,
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse

from .forms import ContactForm, NewsLetterForm, ReviewForm, BookForm

from .models import Book, Genre, Review

# Listing Permission codenames

# from django.contrib.auth.models import Permission
# from django.contrib.contenttypes.models import ContentType

# content_type = ContentType.objects.get_for_model(Book)
# post_permission = Permission.objects.filter(content_type=content_type)
# print([perm.codename for perm in post_permission])


class HomePageView(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filter_object = Book.objects.filter(
            copies_sold__gt=0).order_by("-copies_sold")

        context['best_selling_book'] = filter_object.first()

        context['books_with_offer'] = filter_object[:5]

        context['popular_books_top'] = filter_object[:4]

        context['popular_books_bottom'] = filter_object[4:]

        context['billboard_books'] = Book.objects.all()[:3:-1]

        context['featured_books'] = filter_object[:4:-1]

        context['genres'] = Genre.objects.all()[:5]

        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(LoginRequiredMixin, View):
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


class NewsLetterView(LoginRequiredMixin, View):
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
                    status=201,  # create code
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


class ReviewView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        book_id = request.POST["book"]
        current_book = Book.objects.get(pk=book_id)

        if form.is_valid():
            form = Review(
                name=request.POST["name"],
                email=request.POST["email"],
                review=request.POST["review"],
                author=self.request.user,
                book=current_book,
            )
            form.save()
            return redirect('book_detail', current_book.slug)
        else:
            book = current_book
            return render(
                request,
                "booksaw/main/detail/book_detail.html",
                {
                    "book": book,
                    "form": form,
                }
            )


class BooksByAuthorView(ListView):
    model = Book
    template_name = "booksaw/main/authors/books_by_author.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_name = self.kwargs["author_name"]

        context["books_by_author"] = Book.objects.filter(
            author=author_name,
        ).order_by("-title")

        return context


class AddBookView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "book/add_book.html"
    permission_required = "add_book"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AllBooksView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Book
    template_name = "book/all_books.html"
    context_object_name = "books"
    permission_required = "view_book"


class UpdateBookView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "book/update_book.html"
    permission_required = "change_book"


class DeleteBookView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = "book/delete_book.html"
    success_url = reverse_lazy("home")
    permission_required = "delete_book"


class AllProductsView(ListView):
    model = Book
    template_name = "all_products.html"
    context_object_name = "books"


class SearchView(ListView):
    model = Book
    template_name = "book/book_search_list.html"
    context_object_name = "book_list"

    def get_queryset(self):
        query = self.request.GET.get("query")
        book_list = Book.objects.filter(
            (Q(title__icontains=query) | Q(author__icontains=query) | Q(tag__name__icontains=query) | Q(
                genre__name__icontains=query) | Q(description__icontains=query))
        ).order_by("-copies_sold")
        return book_list
