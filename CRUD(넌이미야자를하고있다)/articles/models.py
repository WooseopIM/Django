from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.TextField()
    contents = models.TextField()
    img_url = models.TextField()

    def __str__(self):
        return f'{self.id} : {self.title}'
