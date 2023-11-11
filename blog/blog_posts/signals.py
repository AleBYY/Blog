from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
import logging
from blog_posts.models import Post, Author

logger = logging.getLogger(__name__)


@receiver(pre_delete, sender=Post)
def log_deleted_object(sender, instance, **kwargs):
    logger.info(f"Object with id {instance.id} of model {sender.__name__} was deleted.")


@receiver(post_save, sender=Post)
def send_email_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'You have created a new post'
        message = f'Your post with the title: {instance}  has been created'
        from_email = settings.EMAIL_HOST_USER
        to_email = instance.user.email
        send_mail(subject, message, from_email, [to_email])
