from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from app.news.models import CategoryModel
from app.news.permission import AdminOrReadOnly
from app.news.serializers import CategorySerializer


class CategoryView(ModelViewSet):
    queryset = CategoryModel.objects.all()
    permission_classes = [AdminOrReadOnly]
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ["name", "id"]
