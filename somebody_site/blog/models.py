from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=False)
    text = models.TextField()
    image = models.ImageField(upload_to='img_post')
