from api.router import router
from posts.viewsets.post_viewset import PostViewSet

router.register(r'post', PostViewSet)
