import graphene
from graphene_django import DjangoObjectType

from addresses.models.address import Address


class AddressType(DjangoObjectType):
    class Meta:
        model = Address
        fields = '__all__'


class Query(graphene.ObjectType):
    all_addresses = graphene.List(AddressType)

    def resolve_all_addresses(root, info):
        return Address.objects.all()


schema = graphene.Schema(query=Query)
