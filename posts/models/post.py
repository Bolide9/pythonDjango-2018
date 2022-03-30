from django.db import models

from posts.models.image import Image
from profiles.models.profile import Profile


class Post(models.Model):
    objects = models.Manager()

    text = models.CharField(max_length=2048, null=True, blank=True)

    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

