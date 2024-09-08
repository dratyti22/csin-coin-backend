from django.urls import path
from rest_framework.routers import SimpleRouter

from app.news.views import CategoryView, NewsView

router = SimpleRouter()

router.register("category", CategoryView, basename="category")
router.register("news", NewsView, basename="news")

urlpatterns = router.urls
