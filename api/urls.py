from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

from addresses.router import router as address
from users.router import router as user
from follows.router import router as follows
from profiles.router import router as profiles
from posts.router import router as posts

urlpatterns = [
    path('', include(address.urls)),
    path('', include(user.urls)),
    path('', include(follows.urls)),
    path('', include(profiles.urls)),
    path('', include(posts.urls)),

    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
