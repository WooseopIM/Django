from django.db import models

# Create your models here.
# 우리가 이제 객체를 생성할 곳
# 상속을 받자

class Article(models.Model):
    title = models.TextField()
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    img_url = models.TextField()

    def __str__(self):
        return f'{self.id} : {self.title}'