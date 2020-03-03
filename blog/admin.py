from django.contrib import admin
from blog.models import Posts


class PostsAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('title', 'slug', 'author', 'created', 'modified')


admin.site.register(Posts, PostsAdmin)
