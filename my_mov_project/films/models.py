from django.db import models


# Create your models here.
class Film(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField()
    review = models.TextField('Отзыв', blank=True)
    image = models.ImageField('Изображение', upload_to='media/films/images/', blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
