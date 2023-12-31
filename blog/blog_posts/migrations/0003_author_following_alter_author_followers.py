# Generated by Django 4.2.3 on 2023-10-07 13:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0002_author_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='author',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='following_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
