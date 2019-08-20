from django.db import models

# Create your models here.
# DB 설계도를 만들었으면 makemigrations

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image_url = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    # 작성자 = 
    # 태그 = 
    # 조회수 = 
    # 추천수 = 
    # 좋아요 = 
    # 댓글 = 