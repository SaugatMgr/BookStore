from django.contrib import admin

from .models import Book, Genre, Tag, Contact, Comment

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(Comment)
