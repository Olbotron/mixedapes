# Generated by Django 5.1.6 on 2025-03-06 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='release_date',
        ),
    ]
