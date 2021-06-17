from django.contrib import admin

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content', 'created_at', 'updated_at')
    list_display_links = ('author', 'title')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Post, PostModelAdmin)
