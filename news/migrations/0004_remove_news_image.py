# Generated by Django 3.0.3 on 2020-02-10 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200210_0750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
    ]
