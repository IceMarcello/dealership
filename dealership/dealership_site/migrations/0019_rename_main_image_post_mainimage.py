# Generated by Django 4.0.5 on 2023-01-24 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dealership_site', '0018_post_main_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='main_image',
            new_name='mainimage',
        ),
    ]