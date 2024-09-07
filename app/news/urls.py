from django.urls import path

from app.news.views import CategoryView

urlpatterns = [
    path("category/", CategoryView.as_view(), name="category"),
]
