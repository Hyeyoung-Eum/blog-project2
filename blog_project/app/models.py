from django.db import models
from datetime import datetime
# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=200)
    category = models.CharField(max_length=20, default=None)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 해당 레코드 생성시 현재 시간 자동저장
    updated_at = models.DateTimeField(null=True, blank=True) # 해당 레코드 갱신시 현재 시간 자동저장

    def __str__(self):
        return self.title

class Comment(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True) #작성 시간 저장
    like = models.PositiveIntegerField(default=0) #좋아요 수 저장

    def __str__(self):
        return self.content

class Reply(models.Model):
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE, null=True) #Comment_id 저장
    content=models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True, null=True) #작성 시간 저장
    like = models.PositiveIntegerField(default=0) #좋아요 수 저장

    def __str__(self):
        return self.content