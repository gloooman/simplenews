# Generated by Django 3.0.3 on 2020-02-05 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200205_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='moderation',
            new_name='premoderation',
        ),
    ]
