from tabnanny import verbose
from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(verbose_name = 'Почта')
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Когда отправлено')


class Category(models.Model):
    title= models.CharField(max_length=50, verbose_name='Категории')
    images = models.ImageField(upload_to='core', verbose_name='Изображение')
    def __str__(self):
        return self.title

# Create your models here.
class FoodCard(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название еды')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='core', verbose_name='Изображение')
    category = models.ForeignKey( Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name