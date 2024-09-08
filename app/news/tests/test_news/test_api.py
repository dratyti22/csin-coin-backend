import json

from app.user.models import User
from django.db.models import F
from django.test import RequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.news.models import CategoryModel, NewsModel, ImageNewsModel
from app.news.serializers import CategorySerializer, ImageSerializer, NewsSerializer


class ApiFileSerializerTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(email='user1@example.com', is_staff=True)
        self.user2 = User.objects.create(email='user2@example.com', key="fsklflasjflfjl2")

        self.category1 = CategoryModel.objects.create(name="Category 1", parent=None)
        self.category2 = CategoryModel.objects.create(name="Category 2", parent=self.category1, description="asd")

        self.news1 = NewsModel.objects.create(title="a", description="a")
        self.news1.category.set([self.category2])

        self.news2 = NewsModel.objects.create(title="s", description="s")
        self.news2.category.set([self.category1])

        self.news3 = NewsModel.objects.create(title="d", description="d")
        self.news3.category.set([self.category1, self.category2])

        self.foto1 = ImageNewsModel.objects.create(news=self.news2,
                                                   image="among-us-space-background-4k-wallpaper-uhdpaper.com-9230f.jpg")

    def test_get(self):
        url = reverse("news-list")
        response = self.client.get(url)
        file = NewsModel.objects.all().prefetch_related("category", "images")
        factory = RequestFactory()
        request = factory.get(url)
        serializer_data = NewsSerializer(file, many=True, context={'request': request}).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    # def test_get_one(self):
    #     url = reverse("File-detail", args=(self.company1.id,))
    #     response = self.client.get(url)
    #     file = File.objects.filter(id=self.company1.id).annotate(
    #         first_name=F("user__first_name"),
    #         last_name=F("user__last_name"),
    #     )
    #     serializer_data = FileSerializer(file, many=True).data
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)
    #     self.assertEqual(serializer_data, [response.data])
    #
    # def test_get_search(self):
    #     url = reverse("File-list")
    #     response = self.client.get(url, data={'search': 'test_company'})
    #     file = File.objects.filter(id__in=[self.company1.id, self.company2.id]).annotate(
    #         first_name=F("user__first_name"),
    #         last_name=F("user__last_name"),
    #     )
    #     serializer_data = FileSerializer(file, many=True).data
    #
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)
    #     self.assertEqual(serializer_data, response.data)

    def test_post(self):
        self.assertEqual(3, NewsModel.objects.all().count())

        url = reverse("news-list")
        data = {
            "title": "asd",
            "description": "asd",
            "category": [
                self.category1.id
            ],
            "uploaded_images": []
        }
        self.client.force_login(self.user1)
        response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, NewsModel.objects.all().count())

    def test_put(self):
        url = reverse("news-detail", args=(self.news2.id,))
        data = {
            'id': self.news2.id,
            "title": "fff",
            "description": "фффффффф",
            "category": [self.category1.id, self.category2.id]
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user1)
        response = self.client.put(url, data=json_data, content_type="application/json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.news2.refresh_from_db()
        self.assertEqual('fff', self.news2.title)

    def test_delete(self):
        self.assertEqual(3, NewsModel.objects.all().count())

        url = reverse("news-detail", args=(self.news3.id,))
        self.client.force_login(self.user1)
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(2, NewsModel.objects.all().count())

    def test_get_one(self):
        url = reverse("news-detail", args=(self.news2.id,))
        response = self.client.get(url)
        file = NewsModel.objects.get(id=self.news2.id)
        serializer = NewsSerializer(file, context={'request': response.wsgi_request})
        serializer_data = serializer.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse("news-list")
        response = self.client.get(url, data={'search': 'a'})
        file = NewsModel.objects.filter(title='a')
        serializer = NewsSerializer(file, many=True, context={'request': response.wsgi_request})
        serializer_data = serializer.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_put_unauthorized(self):
        url = reverse("news-detail", args=(self.news2.id,))
        data = {
            'id': self.news2.id,
            "title": "fff",
            "description": "фффффффф",
            "category": [self.category1.id, self.category2.id]
        }
        json_data = json.dumps(data)
        response = self.client.put(url, data=json_data, content_type="application/json")
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_delete_unauthorized(self):
        url = reverse("news-detail", args=(self.news3.id,))
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_filter_by_time_created(self):
        url = reverse("news-list")
        filter_params = {'time_created__gte': '2024-09-7', 'time_created__lte': '2024-09-9'}
        response = self.client.get(url, filter_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # Only news2 should be in the response

    def test_filter_by_time_created_invalid_params(self):
        url = reverse("news-list")
        filter_params = {'time_created__gte': '2024-10-01', 'time_created__lte': '2024-09-30'}
        response = self.client.get(url, filter_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
