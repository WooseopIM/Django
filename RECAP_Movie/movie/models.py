from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    audience = models.IntegerField()
    open_date = models.DateTimeField()
    genre = models.CharField(max_length=30)
    watch_grade = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
    
    class Meta:
        ordering = ('-pk',)
    
    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'movie_pk': self.pk})



class Review(models.Model):
    content = models.CharField(max_length=200)
    score = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('-pk',)