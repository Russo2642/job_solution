from django.contrib import admin

from .models import Comment, Post, Rating

admin.site.register(Rating)
admin.site.register(Post)
admin.site.register(Comment)
