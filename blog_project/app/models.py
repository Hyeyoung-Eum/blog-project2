from django.db import models

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=200)
    category = models.CharField(max_length=20, default=None)
    content=models.TextField()

    def __str__(self):
        return self.title