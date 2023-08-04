from django.db import models
# Create your models here.


class Main(models.Model):
    first_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='img_photo')


