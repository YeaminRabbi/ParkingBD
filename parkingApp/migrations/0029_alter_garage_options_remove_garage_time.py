# Generated by Django 4.1.2 on 2022-12-06 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0028_booking_start_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='garage',
            options={},
        ),
        migrations.RemoveField(
            model_name='garage',
            name='time',
        ),
    ]
