from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_email(message):
    subject = 'Django App Email'
    email_from = settings.EMAIL_HOST_USER
    return send_mail(subject, message, email_from, settings.EMAIL_RECIPIENTS)