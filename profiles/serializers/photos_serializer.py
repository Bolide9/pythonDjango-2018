from profiles.models.profile import Photos
from common.base_serializer import BaseSerializer


class PhotosSerializer(BaseSerializer):

    class Meta:
        model = Photos
        fields = ['small', 'large']
