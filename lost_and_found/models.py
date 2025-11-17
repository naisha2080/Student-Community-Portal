from django.db import models
from django.contrib.auth.models import User

class LostFoundItem(models.Model):
    STATUS_CHOICES = [
        ('Lost', 'I lost something'),
        ('Found', 'I found something'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    item_name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100, help_text="E.g., Library, Canteen, Block-A")

    # blank=True and null=True so uploading an image is OPTIONAL
    # Files will be saved in 'lost_found_pics/' folder inside media directory, install pillow for imagefield
    image = models.ImageField(upload_to='lost_found_pics/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    is_claimed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.status}: {self.item_name} at {self.location}"

