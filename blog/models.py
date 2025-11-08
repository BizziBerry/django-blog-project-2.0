from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']