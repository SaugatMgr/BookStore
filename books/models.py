from django.db import models


class Category(models.Model):
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
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    # Many to Many relationship with Book
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
