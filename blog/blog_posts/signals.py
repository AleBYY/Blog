from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
import logging
from .tasks import send_email_notification
import requests

from blog_comments.models import Comment
from blog_posts.models import Post, Author

logger = logging.getLogger(__name__)


@receiver(pre_delete, sender=Post)
def log_deleted_object(sender, instance, **kwargs):
    logger.info(f"Object with id {instance.id} of model {sender.__name__} was deleted.")


# @receiver(post_save, sender=Post)
# def send_email_notification(sender, instance, created, **kwargs):
#     if created:
#         subject = 'You have created a new post'
#         message = f'Your post with the title: {instance}  has been created'
#         from_email = settings.EMAIL_HOST_USER
#         to_email = instance.user.email
#         send_mail(subject, message, from_email, [to_email])
# @receiver(post_save, sender=Post)
# def post_save_send_email_notification(sender, instance, created, **kwargs):
#     if created:
#         send_email_notification.delay(instance.id)


# @receiver(post_save, sender=Post)
# def create_comment_on_post_creation(sender, instance, created, **kwargs):
#     if created:
#         Comment.objects.create(
#             post=instance,
#             content="Please follow the rules of conduct in comments.",
#             author=Author.objects.get(username='system'),
#         )
