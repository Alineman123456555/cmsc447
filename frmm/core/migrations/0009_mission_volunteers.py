# Generated by Django 2.1.4 on 2018-12-11 17:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_auto_20181211_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='volunteers',
            field=models.ManyToManyField(blank=True, related_name='volunteer_missions', to=settings.AUTH_USER_MODEL),
        ),
    ]
