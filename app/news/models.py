from django.db import models
from mptt.fields import TreeForeignKey


class CategoryModel(models.Model):
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
        return f"{self.name}-{self.time_created}"
