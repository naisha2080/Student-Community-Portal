from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PYQ(models.Model):
    course_name = models.CharField(max_length=200)
    subject_name = models.CharField(max_length=200)
    year = models.IntegerField()

# Files will be saved in a pyqs/ folder inside media directory
    pyq_file = models.FileField(upload_to='pyqs/')
# Automatic timing    
    uploaded_at = models.DateTimeField(auto_now_add=True)
# links post to a specific user
# If the linked User is deleted, all related records in this model will also be deleted, that is what on_delete does brodah
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Course = {self.course_name} Subject = {self.subject_name} Year = {self.year}"
    
    def filename(self):
        return self.pyq_file.name.split('/')[-1]
