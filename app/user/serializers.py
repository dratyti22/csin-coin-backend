from rest_framework import  serializers

from .models import User


class ProfileUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'middle_name', 'status', 'balance', "date_of_birth", "key", "status")
