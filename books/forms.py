from django import forms

from .models import Contact, NewsLetter, Review, Book


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = "__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "name",
            "email",
            "review",
        ]
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('slug', 'copies_sold',)