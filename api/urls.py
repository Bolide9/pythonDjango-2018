from django.contrib import admin
from django.urls import path, include

from users.router import router as user
from events.router import router as event


urlpatterns = [
    path('', include(user.urls)),
    path('', include(event.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
