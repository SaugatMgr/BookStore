from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=64)
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


class NameEmailField(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()

    class Meta:
        # Don't make table of this class/model
        abstract = True


class Comment(NameEmailField):
    comment = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.comment[:25]}"


class Contact(NameEmailField):
    message = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.message[:25]}"


class NewsLetter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
