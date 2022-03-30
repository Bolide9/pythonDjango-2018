from rest_framework import serializers

from follows.models.follow import Follow
from profiles.serializers.photos_serializer import PhotosSerializer
from users.models import CustomUser
from common.base_serializer import BaseSerializer


class UserSerializer(BaseSerializer):
    name = serializers.CharField(source='first_name')

    followed = serializers.SerializerMethodField()
    photos = serializers.SerializerMethodField()

    def get_followed(self, user):
        me = self.context['request'].user

        if me.is_anonymous:
            return False

        return Follow.objects.filter(follower=me, followed=user).exists()

    def get_photos(self, user):
        photos = user.profile.photos
        return PhotosSerializer(photos).data

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'name', 'first_name', 'last_name', 'photos', 'followed']
