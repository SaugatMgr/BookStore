from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse


class TimeStamp(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # Don't make table of this class/model
    class Meta:
        abstract = True


class NameEmailField(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()

    class Meta:
        # Don't make table of this class/model
        abstract = True


class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Book(TimeStamp):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    author = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    book_cover = models.ImageField(upload_to='covers/', blank=True)
    copies_sold = models.PositiveBigIntegerField(default=0)

    # 1 to Many relationship with Book
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
    )

    # Many to Many relationship with Book
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})


class Review(NameEmailField, TimeStamp):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.name}: {self.review[:30]}"


class Contact(NameEmailField, TimeStamp):
    message = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.message[:25]}"


class NewsLetter(TimeStamp):
    email = models.EmailField()

    def __str__(self):
        return self.email
