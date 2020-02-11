from django.db import models
from tinymce import HTMLField
from django.urls import reverse
from django.db.models import signals
from simplenews.task import send_verification_email, send_comment_notifications
from users.models import CustomUser
from django.contrib.auth import get_user_model


class News(models.Model):
    NEW = 'NEW'
    APR = 'APR'
    DEC = 'DEC'
    STATUS_CHOICES = [
        (NEW, 'Новый'),
        (APR, 'Одобрен'),
        (DEC, 'Отклонен')
    ]
    article = models.CharField('Заголовок', max_length=120)
    text = HTMLField('Контент')
    status = models.CharField('Статус', max_length=3, choices=STATUS_CHOICES, default=NEW)
    author = models.ForeignKey(get_user_model(), verbose_name='Автор новости',
                               on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='static/media/images/', blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'{self.article} ({self.author}), {self.status}'

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'id': self.id})

    # def save(self, **kwargs):
    #     super(News, self).save(self, **kwargs)


class Comment(models.Model):
    news = models.ForeignKey(News, verbose_name='Новость', on_delete=models.CASCADE)
    email = models.EmailField('Email-адресс')
    text = models.TextField('Текст коментария')
    create = models.DateTimeField(auto_now_add=True)


def comment_post_save(sender, instance, signal, *args, **kwargs):
    news = instance.news
    send_comment_notifications.delay(news)


signals.post_save.connect(comment_post_save, sender=Comment)

