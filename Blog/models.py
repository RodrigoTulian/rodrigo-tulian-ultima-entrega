from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = RichTextField()
    image = models.ImageField(upload_to="posts/")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title