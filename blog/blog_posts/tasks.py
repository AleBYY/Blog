from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Post

@shared_task
def send_email_notification(post_id):
    post = Post.objects.get(pk=post_id)
    subject = 'You have created a new post'
    message = f'Your post with the title: {post.name} has been created'
    from_email = settings.EMAIL_HOST_USER
    to_email = post.user.email
    send_mail(subject, message, from_email, [to_email])