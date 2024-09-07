from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

class CategoryModel(MPTTModel):
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    name = models.CharField(max_length=255, verbose_name="Название категории")
    description = models.TextField(verbose_name="Описание категории", blank=True, null=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
        verbose_name='Родительская категория'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        db_table = 'news_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.name} - {self.time_created}"

class NewsModel(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок новости")
    description = models.TextField(verbose_name="Описание")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        db_table = 'news'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f"{self.title} - {self.time_created}"

class ImageNewsModel(models.Model):
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE, verbose_name="Новость", related_name="images")
    image = models.ImageField(upload_to='media/news_images/', verbose_name="Изображение")

    class Meta:
        db_table = 'news_image'
        verbose_name = 'Изображение новости'
        verbose_name_plural = 'Изображения новостей'

    def __str__(self):
        return f"{self.news.title}"