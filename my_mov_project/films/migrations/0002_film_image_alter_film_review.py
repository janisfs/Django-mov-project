# Generated by Django 5.1.3 on 2024-11-18 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='image',
            field=models.ImageField(blank=True, upload_to='films/images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='film',
            name='review',
            field=models.TextField(blank=True, verbose_name='Отзыв'),
        ),
    ]
