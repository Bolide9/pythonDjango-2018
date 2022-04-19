from django.db.models import Q
from django_filters import FilterSet, CharFilter
from graphene import relay
from graphene_django import DjangoObjectType
from users.models import CustomUser


class CustomFilter(FilterSet):
    value = CharFilter(method='custom_filter', label="Search")

    def custom_filter(self, queryset, name, value):
        return CustomUser.objects.filter(Q(first_name__startswith=value) | Q(last_name__startswith=value)
                                         | Q(email__startswith=value) | Q(username__startswith=value))

    class Meta:
        model = CustomUser
        fields = ['value']


class CustomNode(DjangoObjectType):
    class Meta:
        model = CustomUser
        filterset_class = CustomFilter
        fields = ['email', 'username', 'first_name', 'last_name']
        interfaces = (relay.Node,)
