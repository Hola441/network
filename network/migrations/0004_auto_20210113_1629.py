# Generated by Django 3.1.2 on 2021-01-13 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_post_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='liked',
            field=models.BooleanField(auto_created=True, default=False),
        ),
    ]
