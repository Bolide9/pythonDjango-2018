from django.db import models


class Image(models.Model):
    img_url = models.CharField(max_length=1024, null=True, blank=True)

