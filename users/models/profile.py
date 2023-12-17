import os

from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300, null=False, blank=False)
    avatar = models.ImageField(upload_to='user_avatars', blank=True)

    def __str__(self):
        return self.user.email

    @property
    def filename(self):
        return os.path.basename(self.image.name)
