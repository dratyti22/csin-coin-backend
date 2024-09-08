import json

from app.user.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.news.models import CategoryModel
from app.news.serializers import CategorySerializer


class ApiCategorySerializerTestCase(APITestCase):
    def setUp(self):
        self.category1 = CategoryModel.objects.create(name="Category 1", parent=None)
        self.category2 = CategoryModel.objects.create(name="Category 2", parent=self.category1, description="asd")

    def test_get(self):
        url = reverse("category-list")
        response = self.client.get(url)
        tag = CategoryModel.objects.all()
        serializer_data = CategorySerializer(tag, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    # def test_get_one(self):
    #     url = reverse("Tags-detail", args=(self.company1.user_id,))
    #     response = self.client.get(url)
    #     tag = CategoryModel.objects.filter(user_id=self.company1.user_id).annotate(
    #         first_name=F("user__first_name"),
    #         last_name=F("user__last_name"),
    #     )
    #     serializer_data = CategorySerializer(tag, many=True).data
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)
    #     self.assertEqual(serializer_data, [response.data])
    #
    # def test_get_search(self):
    #     url = reverse("tags-list")
    #     response = self.client.get(url, data={'search': 'test_company'})
    #     tag = CategoryModel.objects.filter(user_id__in=[self.company1.user_id, self.company2.user_id]).annotate(
    #         first_name=F("user__first_name"),
    #         last_name=F("user__last_name"),
    #     )
    #     serializer_data = CategorySerializer(tag, many=True).data
    #
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)
    #     self.assertEqual(serializer_data, response.data)

    def test_post(self):
        user3 = User.objects.create(username='test_user3', is_staff=True)
        self.assertEqual(2, CategoryModel.objects.all().count())

        url = reverse("category-list")

        data = {
            "name": "Category 1",
            "description": "",
            "parent": None,
        }

        json_data = json.dumps(data)
        self.client.force_login(user3)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, CategoryModel.objects.all().count())

    def test_put(self):
        user3 = User.objects.create(username='test_user3', is_staff=True)

        url = reverse("category-detail", args=(self.category1.id,))
        data = {
            "name": "Category 1",
            "description": "asd",
            "parent": None,
        }
        json_data = json.dumps(data)
        self.client.force_login(user3)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.category1.refresh_from_db()
        self.assertEqual('asd', self.category1.description)

    def test_delete(self):
        user3 = User.objects.create(username='test_user3', is_staff=True)
        self.assertEqual(2, CategoryModel.objects.all().count())

        url = reverse("category-detail", args=(self.category2.id,))
        self.client.force_login(user3)
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(1, CategoryModel.objects.all().count())
