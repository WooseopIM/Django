from django.contrib import admin
from .models import Article, Comment

# Register your models here.

# 뭐를 보고 싶은지?
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
    list_display_links = ('title',)

admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'comment', 'created_at', 'updated_at')

admin.site.register(Comment, CommentAdmin)