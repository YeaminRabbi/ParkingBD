# Generated by Django 4.1.2 on 2022-12-02 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0014_remove_booking_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='location',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
