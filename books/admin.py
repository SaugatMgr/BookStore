from django.contrib import admin

from .models import Book, Genre, Tag

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Tag)
