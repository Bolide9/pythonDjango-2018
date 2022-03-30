from common.base_serializer import BaseSerializer
from profiles.models.profile import Profile
from profiles.serializers.photos_serializer import PhotosSerializer


class ProfileSerializer(BaseSerializer):
    photos = PhotosSerializer()

    class Meta:
        model = Profile
        fields = '__all__'
