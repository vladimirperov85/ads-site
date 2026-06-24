from django.db import models
from django.contrib.auth.models import User


class Ad(models.Model):
    """Модель объявления"""
    # Категории автомобилей
    CAR_CATEGORIES = [
        ('sedan', 'Седан'),
        ('crossover', 'Кроссовер'),
        ('suv', 'Внедорожник'),
    ]
    
    # Бренды автомобилей
    CAR_BRANDS = [
        ('Toyota', 'Toyota'),
        ('Honda', 'Honda'),
        ('Ford', 'Ford'),
        ('VW', 'VW'),
        ('BMW', 'BMW'),
        ('Mercedes', 'Mercedes'),
        ('Audi', 'Audi'),
        ('Hyundai', 'Hyundai'),
        ('KIA', 'KIA'),
        ('LADA', 'LADA'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    image = models.ImageField(upload_to='ads/', blank=True, null=True, verbose_name='Изображение')
    
    # Новые поля для фильтрации
    category = models.CharField(
        max_length=20,
        choices=CAR_CATEGORIES,
        verbose_name='Категория'
    )
    car_brand = models.CharField(
        max_length=20,
        choices=CAR_BRANDS,
        verbose_name='Бренд'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']
