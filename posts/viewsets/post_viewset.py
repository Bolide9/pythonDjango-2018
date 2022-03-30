import datetime

from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
from common.base_viewset import BaseViewSet
from posts.models.post import Post
from posts.serializers.post_serializer import PostSerializer


MAX_POSTS_TODAY = 1


class PostViewSet(BaseViewSet):
    date_gte = timezone.now() - datetime.timedelta(minutes=5)

    queryset = Post.objects.filter(created_at__gte=date_gte)
    serializer_class = PostSerializer

    # def get(self):
    #     posts = Post.objects.all()
    #     serializer = self.get_serializer(posts)
    #     return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        posts = Post.objects.filter(created_at__gte=self.date_gte)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if posts.count() > MAX_POSTS_TODAY:
            return JsonResponse({'exception': 'not valid'},  status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

