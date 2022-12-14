# Generated by Django 4.0.5 on 2022-10-20 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealership_site', '0009_post_fuel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_price', models.FloatField()),
                ('exchange', models.FloatField(choices=[('EUR', 4.7878), ('USD', 4.896502352219268), ('CHF', 4.88053007135576), ('SEK', 0.4374497478254513), ('PLN', 1.0)], default='PLN')),
                ('transport_cost', models.FloatField()),
                ('vat', models.FloatField()),
            ],
        ),
    ]
