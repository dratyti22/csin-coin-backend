from .models import CategoryModel, NewsModel, ImageNewsModel

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["id", "name", "description", "parent", "time_created"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNewsModel
        fields = ["image"]


class NewsSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True, required=False
    )

    class Meta:
        model = NewsModel
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop("uploaded_images", None)
        category = validated_data.pop("category", None)
        news = NewsModel(**validated_data)
        news.save()
        news.category.set(category)
        if images_data:
            for image in images_data:
                ImageNewsModel.objects.create(description_file=news, image=image)
        return news
