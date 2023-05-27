from django.contrib import admin

from .models import Rating, Comment, Post

admin.site.register(Rating)
admin.site.register(Post)
admin.site.register(Comment)
