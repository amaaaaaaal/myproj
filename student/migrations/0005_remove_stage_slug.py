# Generated by Django 5.0.4 on 2024-04-24 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_stage_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stage',
            name='slug',
        ),
    ]
