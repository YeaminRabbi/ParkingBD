# Generated by Django 4.1.2 on 2022-12-06 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0023_booking_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='garage',
            name='allow_hourly',
        ),
        migrations.RemoveField(
            model_name='garage',
            name='allow_monthly',
        ),
    ]
