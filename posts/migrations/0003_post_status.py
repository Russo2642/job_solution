# Generated by Django 4.1.7 on 2023-12-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('UNVERIFIED', 'Не проверен'), ('VERIFIED', 'Проверен'), ('AWAITING', 'Ожидает проверки')], default='UNVERIFIED', max_length=100, verbose_name='Статус'),
        ),
    ]