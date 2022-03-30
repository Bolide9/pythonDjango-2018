from users.models import CustomUser
from django.db import models


class Photos(models.Model):
    objects = models.Manager()

    small = models.CharField(max_length=8000, null=True, blank=True)
    large = models.CharField(max_length=8000, null=True, blank=True)

    def __str__(self):
        return f'{self.small} {self.large}'

    class Meta:
        verbose_name_plural = 'Photos'


class Contacts(models.Model):
    github = models.CharField(max_length=1024, null=True, blank=True)
    vk = models.CharField(max_length=1024, null=True, blank=True)
    facebook = models.CharField(max_length=1024, null=True, blank=True)
    instagram = models.CharField(max_length=1024, null=True, blank=True)
    twitter = models.CharField(max_length=1024, null=True, blank=True)
    website = models.CharField(max_length=1024, null=True, blank=True)
    youtube = models.CharField(max_length=1024, null=True, blank=True)
    mainLink = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return f'{self.github}'

    class Meta:
        verbose_name_plural = 'Contacts'


class Profile(models.Model):
    objects = models.Manager()

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    contacts = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True, blank=True)
    photos = models.ForeignKey(Photos, on_delete=models.SET_NULL, null=True, blank=True)

    lookingForAJob = models.BooleanField(default=False, null=True, blank=True)
    lookingForAJobDescription = models.CharField(max_length=2048, null=True, blank=True)
    status = models.CharField(max_length=1024, null=True)

    def __str__(self):
        return f'{self.user}'
