# Generated by Django 4.1.7 on 2023-12-19 16:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Comment body')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_of_activity', models.CharField(choices=[('DEVELOPMENT', 'Разработка'), ('DESIGN', 'Дизайн'), ('OTHER', 'Другое')], default='OTHER', max_length=100, verbose_name='Сфера деятельности')),
                ('title', models.CharField(max_length=3000, verbose_name='Заголовок')),
                ('company', models.CharField(max_length=1000, verbose_name='Работодатель')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Сайт')),
                ('location', models.CharField(max_length=1000, null=True, verbose_name='Локация')),
                ('position', models.CharField(max_length=300, verbose_name='Должность')),
                ('work_time_from', models.DateField()),
                ('work_time_to', models.DateField(blank=True, null=True)),
                ('body', models.TextField(verbose_name='Post body')),
                ('negative', models.TextField(null=True, verbose_name='Post negative')),
                ('positive', models.TextField(null=True, verbose_name='Post positive')),
                ('ensemble', models.CharField(choices=[('POSITIVELY', 'Положительно'), ('NEUTRAL', 'Нейтрально'), ('NEGATIVE', 'Отрицательно')], default='NEUTRAL', max_length=30, verbose_name='Общее впечатление')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('team', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('education', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('management', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('social_package', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('office_comfort', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
    ]