# Generated by Django 4.1.2 on 2022-12-01 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0010_address_remove_booking_locality_alter_booking_garage'),
    ]

    operations = [
        migrations.AddField(
            model_name='garage',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='garage',
            name='lng',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
