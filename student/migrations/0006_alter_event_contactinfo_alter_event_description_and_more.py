# Generated by Django 5.0.4 on 2024-04-24 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_remove_stage_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contactInfo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='intitule',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='lieu',
            field=models.CharField(max_length=200),
        ),
    ]
