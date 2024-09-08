# from rest_framework.test import APITestCase
#
# from app.news.models import CategoryModel
# from app.news.serializers import CategorySerializer
# from app.user.models import User
#
#
# class CategoryModelSerializerTestCase(APITestCase):
#     def setUp(self):
#         self.user1 = User.objects.create(email='user1@example.com')
#         self.category1 = CategoryModel.objects.create(name="Category 1", parent=None, time_created="2024-09-07T16:39:08.890866Z")
#         self.category2 = CategoryModel.objects.create(name="Category 2", parent=self.category1, description="asd", time_created="2024-09-07T16:39:08.890866Z")
#         self.category_test = CategoryModel.objects.all().order_by("id")
#
#     def test_ok(self):
#         data = CategorySerializer(self.category_test, many=True).data
#         expect_data = [
#             {
#                 "id": self.category1.id,
#                 "name": "Category 1",
#                 "description": "",
#                 "parent": None,
#                 'time_created': "2024-09-07T16:39:08.890866Z"
#             },
#             {
#                 "id": self.category2.id,
#                 "name": "Category 2",
#                 "description": "asd",
#                 "parent": self.category1.id,
#                 'time_created': "2024-09-07T16:39:08.890866Z"
#             },
#         ]
#         print(expect_data)
#         print(data)
#         self.assertEqual(expect_data, data)
