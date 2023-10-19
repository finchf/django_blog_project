from django.contrib import admin

from .models import Topic, Article, Comment, UserTopic

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author')
    list_filter = ('topics', )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'created_at', 'author')

@admin.register(UserTopic)
class UserTopicAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic', 'prefers', 'notify')
