import graphene
from graphene_django import DjangoObjectType

from profiles.models.profile import Photos
from users.models import CustomUser


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'

#
# class PhotosType(DjangoObjectType):
#     class Meta:
#         model = Photos
#         fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(CustomUserType)

    def resolve_all_users(root, info):
        return CustomUser.objects.all()


schema = graphene.Schema(query=Query)
