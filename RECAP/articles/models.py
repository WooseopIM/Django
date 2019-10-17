from django.db import models
from django.urls import reverse

# Create your models here.
# 모델은 title, content, created_at, updated_at

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-pk',)

    # method도 추가예정
    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'article_pk': self.pk})


class Comment(models.Model):
    comment = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.comment

    # def get_absolute_url(self):
    #     return reverse('articles:detail', kwargs={'article_pk':self.article.pk})