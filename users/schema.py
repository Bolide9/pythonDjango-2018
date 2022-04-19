import graphene
from django.db.models import Q

from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from users.filters.custom_filter import CustomNode
from users.models import CustomUser


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(CustomUserType)
    search_by_value = graphene.List(CustomUserType, value=graphene.String(required=True))

    # EXAMPLE 1
    search_by_val = DjangoFilterConnectionField(CustomNode)

    # EXAMPLE 2
    def resolve_search_by_value(self, info, value):
        users = CustomUser.objects.filter(Q(first_name__startswith=value) | Q(last_name__startswith=value)
                                          | Q(email__startswith=value) | Q(username__startswith=value))
        return users

    def resolve_all_users(self, info):
        return CustomUser.objects.all()


schema = graphene.Schema(query=Query)
