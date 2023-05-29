from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Comment(models.Model):
    post = models.ForeignKey(
        to='posts.Post',
        related_name='comments',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        to=get_user_model(),
        related_name='post_comments',
        null=True,
        on_delete=models.SET_NULL,
    )
    body = models.TextField(_('Comment body'), null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.body[:20]} by {self.author.email}'
