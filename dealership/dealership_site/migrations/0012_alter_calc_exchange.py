# Generated by Django 4.0.5 on 2022-10-27 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealership_site', '0011_alter_calc_exchange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calc',
            name='exchange',
            field=models.FloatField(choices=[(4.7548, 'EUR'), (4.743889055173103, 'USD'), (4.7945951396591715, 'CHF'), (0.43410937642654984, 'SEK'), (1.0, 'PLN')], default='PLN'),
        ),
    ]
