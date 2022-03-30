from django.contrib import admin

from posts.models.post import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
