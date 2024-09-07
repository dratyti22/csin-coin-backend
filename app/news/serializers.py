
from .models import CategoryModel

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

