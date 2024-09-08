from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.viewsets import ModelViewSet

from app.news.models import CategoryModel, NewsModel
from app.news.permission import AdminOrReadOnly
from app.news.serializers import CategorySerializer, NewsSerializer


class CategoryView(ModelViewSet):
    queryset = CategoryModel.objects.all()
    permission_classes = [AdminOrReadOnly]
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ["name", "id"]


class NewsView(ModelViewSet):
    queryset = NewsModel.objects.all().prefetch_related("category", "images")
    permission_classes = [AdminOrReadOnly]
    serializer_class = NewsSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["title", "id", "time_created"]
    filterset_fields = ["time_created"]
    parser_classes = (MultiPartParser, FormParser, JSONParser)
