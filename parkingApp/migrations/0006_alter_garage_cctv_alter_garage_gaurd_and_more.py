# Generated by Django 4.1.2 on 2022-11-25 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0005_remove_garage_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garage',
            name='CCTV',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='garage',
            name='Gaurd',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='garage',
            name='Indoor',
            field=models.BooleanField(),
        ),
    ]
