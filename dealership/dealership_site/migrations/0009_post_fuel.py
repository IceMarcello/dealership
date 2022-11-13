# Generated by Django 4.0.5 on 2022-10-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealership_site', '0008_alter_post_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fuel',
            field=models.CharField(choices=[('Diesel', 'Diesel'), ('Gas', 'Gas'), ('Hybrid', 'Hybrid'), ('Electric', 'Electric'), ('Other', 'Other')], default='Other', max_length=10),
        ),
    ]