from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Rating(models.Model):
    article = models.ForeignKey(
        to='posts.Post',
        related_name='article_rating',
        on_delete=models.CASCADE,
        default=0,
    )
    salary = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    team = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    education = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    management = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    social_package = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    office_comfort = models.SmallIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
