# Generated by Django 4.1.2 on 2022-11-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0007_alter_garage_allow_hourly_alter_garage_allow_monthly'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garage',
            name='CCTV',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='garage',
            name='Gaurd',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='garage',
            name='Indoor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='garage',
            name='allow_hourly',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='garage',
            name='allow_monthly',
            field=models.BooleanField(default=True),
        ),
    ]