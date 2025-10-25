from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название категории")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок новости")
    subtitle = models.CharField(max_length=300, verbose_name="Подзаголовок новости",)
    image = models.ImageField(upload_to='newsimages/', verbose_name="Изображение новости")
    content = models.TextField(verbose_name="Содержание новости")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="news", verbose_name="Категория")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
