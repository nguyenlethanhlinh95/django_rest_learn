from django.db import models
from django.apps import AppConfig

# Create your models here.

class Post(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title