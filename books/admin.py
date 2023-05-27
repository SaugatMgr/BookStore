from django.contrib import admin

from .models import Book, Genre, Tag, Contact, Review, NewsLetter

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(Review)
admin.site.register(NewsLetter)
