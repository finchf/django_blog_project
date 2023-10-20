from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=255)
    subscribers = models.ManyToManyField(User, related_name='topics')

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    topics = models.ManyToManyField(Topic, related_name='articles_on_topic')

    def __str__(self):
        return self.title

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.message






