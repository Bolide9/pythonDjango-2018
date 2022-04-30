from rest_framework import serializers

from users.models import CustomUser
from common.base_serializer import BaseSerializer


class UserSerializer(BaseSerializer):
    name = serializers.CharField(source='first_name')

    class Meta:
        model = CustomUser
        fields = '__all__'
