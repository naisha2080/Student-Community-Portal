from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    course_name = models.CharField(max_length=200)
    subject_name = models.CharField(max_length=200)
    topic_name = models.CharField(max_length=200)


    # files will be stored in a notes/ folder inside media directory
    note_file = models.FileField(upload_to='notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Course = {self.course_name} Subject = {self.subject_name} Topic = {self.topic_name}"
    
    def filename(self):
        return self.note_file.name.split('/')[-1]


