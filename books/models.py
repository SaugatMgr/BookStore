from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)


class Tag(models.Model):
    name = models.CharField(max_length=64)


class Book(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    author = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    book_cover = models.ImageField(upload_to='covers/', blank=True)
    copies_sold = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title
