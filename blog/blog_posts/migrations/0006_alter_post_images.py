# Generated by Django 4.2.3 on 2023-10-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0005_post_disliked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='blog_posts/post_tbs/'),
        ),
    ]
