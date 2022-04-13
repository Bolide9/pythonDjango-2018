import graphene

from users.schema import Query as UsersQuery
from profiles.schema import Query as ProfileQuery
from addresses.schema import Query as AddressesQuery
from posts.schema import Query as PostsQuery


class Query(UsersQuery, ProfileQuery, AddressesQuery, PostsQuery, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=Query)
