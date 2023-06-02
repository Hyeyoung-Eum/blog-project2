from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20, default=None)

    def __str__(self):
        return self.name
    #위의 category와 연결이 되어있진 않음.

class Article(models.Model):
    title=models.CharField(max_length=200)
    category = models.ForeignKey(Category, verbose_name="카테고리",on_delete=models.CASCADE)
    content=models.TextField()
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title