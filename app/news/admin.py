from django.contrib import admin

from .models import CategoryModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parent', 'time_created']
    list_filter = ["id"]
    search_fields = ["id"]
