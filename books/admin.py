from django.contrib import admin

from .models import Book, Genre, Tag, Contact, Review, NewsLetter

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price',)
    prepopulated_fields = {
        "slug": ("title", ),
    }

admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(Review)
admin.site.register(NewsLetter)
