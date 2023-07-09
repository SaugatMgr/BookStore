from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from books.models import Book


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    profile_img = models.ImageField(default="default.jpg", upload_to="Profile/")

    def __str__(self):
        return f"{self.user} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.profile_img.path)

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)

            # create a thumbnail
            img.thumbnail(output_size)

            # override the large image
            img.save(self.profile_img.path)
