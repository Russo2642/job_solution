from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Rating(models.Model):
    post = models.ForeignKey(
        to='posts.Post',
        related_name='post_rating',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        to=get_user_model(),
        related_name='author_rating',
        null=True,
        on_delete=models.CASCADE,
    )
    salary = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    team = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    education = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    management = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    social_package = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    office_comfort = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self):
        return f"{self.post}"
