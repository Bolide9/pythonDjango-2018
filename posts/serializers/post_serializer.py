from common.base_serializer import BaseSerializer
from posts.models.post import Post


class PostSerializer(BaseSerializer):

    class Meta:
        model = Post
        fields = '__all__'
