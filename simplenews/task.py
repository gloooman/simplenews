from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from simplenews.celery import app
from simplenews.settings import EMAIL_HOST_USER


@app.task
def send_verification_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            'Verify your QuickPublisher account',
            'Follow this link to verify your account: '
                'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
            EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
    except UserModel.DoesNotExist:
        print("Tried to send verification email to non-existing user '%s'" % user_id)


@app.task
def send_comment_notifications(news):
    email = news.author.email
    try:
        send_mail(
            f'Вашу новость {news.article} прокоментировали',
            f'Перейти к новости {news.get_absolute_url()}',
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

    except:
        print("Tried to send comment notifications to non-existing to "+email)
