from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class FieldOfActivityChoice(models.TextChoices):
    DEVELOPMENT = 'DEVELOPMENT', 'Разработка'
    DESIGN = 'DESIGN', 'Дизайн'
    MARKETING = 'MARKETING', 'Маркетинг'
    ADMINISTRATION = 'ADMINISTRATION', 'Администрирование'
    APPLIED_TECHNOLOGIES = 'APPLIED_TECHNOLOGIES', 'Прикладные технологии'
    OTHER = 'OTHER', 'Другое'


class EnsembleChoice(models.TextChoices):
    POSITIVELY = 'POSITIVELY', 'Положительно'
    NEUTRAL = 'NEUTRAL', 'Нейтрально'
    NEGATIVE = 'NEGATIVE', 'Отрицательно'


class StatusChoice(models.TextChoices):
    UNVERIFIED = 'UNVERIFIED', 'Не проверен'
    VERIFIED = 'VERIFIED', 'Проверен'
    AWAITING = 'AWAITING', 'Ожидает проверки'


class Post(models.Model):
    author = models.ForeignKey(
        to=get_user_model(),
        related_name='posts',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Автор',
    )
    field_of_activity = models.CharField(
        choices=FieldOfActivityChoice.choices,
        default=FieldOfActivityChoice.OTHER,
        max_length=100,
        verbose_name='Сфера деятельности',
    )
    title = models.CharField(
        max_length=3000,
        null=False,
        verbose_name='Заголовок',
    )
    company = models.CharField(max_length=1000, null=False, blank=False, verbose_name='Работодатель')
    website = models.URLField(null=True, blank=True, verbose_name='Сайт')
    location = models.CharField(max_length=1000, null=True, verbose_name='Локация')
    position = models.CharField(max_length=300, null=False, verbose_name='Должность')
    work_time_from = models.DateField(null=False, blank=False)
    work_time_to = models.DateField(null=True, blank=True)
    body = models.TextField(_('Post body'), null=False)
    negative = models.TextField(_('Post negative'), null=True)
    positive = models.TextField(_('Post positive'), null=True)
    ensemble = models.CharField(
        choices=EnsembleChoice.choices,
        default=EnsembleChoice.NEUTRAL,
        max_length=30,
        verbose_name='Общее впечатление',
    )
    likes = models.ManyToManyField(
        to=get_user_model(),
        related_name='post_likes',
        blank=True,
        null=True,
    )
    views = models.ManyToManyField(
        to=get_user_model(),
        related_name='post_views',
        blank=True,
        null=True,
    )
    status = models.CharField(
        choices=StatusChoice.choices,
        default=StatusChoice.UNVERIFIED,
        max_length=100,
        verbose_name='Статус',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.title} by {self.author.email}'
