from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from .managers import CustomUserManager
from django.db.models import signals
from simplenews.task import send_verification_email


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('Email-адресс', unique=True)
    first_name = models.CharField('Имя', max_length=120, blank=True)
    last_name = models.CharField('Фамилия', max_length=120, blank=True)
    birthday = models.DateField('День рождения', blank=True, null=True)
    premoderation = models.BooleanField("Премодерация", default=True)
    is_verified = models.BooleanField('Подтверждение', default=False)
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        send_verification_email.delay(instance.pk)


signals.post_save.connect(user_post_save, sender=CustomUser)