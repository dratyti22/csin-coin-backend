from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.tokens import default_token_generator
from django.db import IntegrityError
from django.shortcuts import render
from django.utils.http import urlsafe_base64_decode
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.service.email import send_activate_email_message
from app.service.tasks import send_activate_email_message_task
from app.user.models import User
from app.user.serializers import ProfileUserSerializer


class CreateUserView(APIView):
    def post(self, request):
        data = request.data
        print(data)
        required_fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number',
                           'password']

        # Проверка наличия всех необходимых полей
        if not all(field in data for field in required_fields):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        email = data.get('email')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        middle_name = data.get('middle_name')
        date_of_birth = data.get('date_of_birth')
        phone_number = data.get('phone_number')
        try:
            User.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                date_of_birth=date_of_birth,
                phone_number=phone_number
            )
        except IntegrityError as e:
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        send_activate_email_message_task.delay(email)

        return Response({'message': 'Account has been created, confirm your account'}, status=status.HTTP_201_CREATED)


class LoginUserView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = authenticate(request, username=email, password=password)
            login(request, user)
            return Response({"success": "You have logged in successfully"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Need to confirm account'}, status=status.HTTP_400_BAD_REQUEST)


class AvtivateUserView(APIView):
    def get(self, request, uid64, token):
        try:
            uid = urlsafe_base64_decode(uid64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return Response({"success": "You have activated your account"}, status=status.HTTP_200_OK)
        else:
            return Response({"failed": "Failed to activate account"}, status=status.HTTP_200_OK)


class LogoutUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"success": "Logged out"}, status=status.HTTP_200_OK)


class ProfileUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = ProfileUserSerializer(user)
        return Response(serializer.data)
