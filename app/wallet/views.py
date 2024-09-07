from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()


class TopUpBalanceView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        pk = request.data.get("id")
        amount = request.data.get("amount")
        message = request.data.get("message")
        user = User.objects.get(id=pk)
        user.balance += amount
        user.save()
        return Response({"success": "Balance replenishment completed", "message": message}, status=status.HTTP_200_OK)
