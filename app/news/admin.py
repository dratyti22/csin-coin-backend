from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import CategoryModel, NewsModel, ImageNewsModel


@admin.register(CategoryModel)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ["tree_actions", "indented_title", 'id', 'description', 'parent']
    list_filter = ["id"]
    search_fields = ["id"]


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'time_created', 'category']
    list_filter = ["id"]
    search_fields = ["id"]


@admin.register(ImageNewsModel)
class ImageNewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'news_name']
    list_filter = ["id"]
    search_fields = ["id"]

    def news_name(self, obj):
        return obj.news.title
