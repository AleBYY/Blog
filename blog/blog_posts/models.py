from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Author(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    profile_pic = models.ImageField(upload_to="blog_posts/profile_pic/",
                                    default='blog_posts/default/avatar.webp')
    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='followers_users')
    followers = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='following_users')

    bio = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Post(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    description = models.TextField(help_text="Enter you blog text here.")
    post_date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='blog_posts/post_images/', blank=True, null=True,
                               default='blog_posts/post_tbs/profile_pic.png')
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    disliked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='disliked_posts', blank=True)

    class Meta:
        ordering = ["-post_date"]

    def __str__(self):
        return self.name
