# Generated by Django 3.1.2 on 2021-01-13 18:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_follow_like_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.ManyToManyField(auto_created=True, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
