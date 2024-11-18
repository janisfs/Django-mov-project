from django.db import models


# Create your models here.
class Film(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField()
    review = models.CharField('Отзыв', max_length=255)
