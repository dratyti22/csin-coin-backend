from django.urls import path
from rest_framework.routers import SimpleRouter

from app.news.views import CategoryView

router = SimpleRouter()

router.register("category", CategoryView)

urlpatterns = router.urls
