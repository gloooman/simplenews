# Generated by Django 3.0.3 on 2020-02-05 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=120, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текс новости')),
                ('status', models.CharField(choices=[('NEW', 'Новый'), ('APR', 'Одобрен'), ('DEC', 'Отклонен')], default='NEW', max_length=3, verbose_name='Статус')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Автор новости')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
