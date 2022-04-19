import graphene
from graphene_django import DjangoObjectType

from follows.models.follow import Follow


class FollowType(DjangoObjectType):
    class Meta:
        model = Follow
        fields = '__all__'


class Query(graphene.ObjectType):
    all_followers = graphene.List(FollowType)

    def resolve_all_followers(self, info):
        return Follow.objects.all()


schema = graphene.Schema(query=Query)
