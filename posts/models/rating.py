from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Rating(models.Model):
    article = models.OneToOneField(
        to='posts.Post',
        related_name='article_rating',
        on_delete=models.CASCADE,
    )
    salary = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=0),
    team = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=0),
    education = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=0),
    management = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=0),
    social_package = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=0),
    office_comfort = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=0),
