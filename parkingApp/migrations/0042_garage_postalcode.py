# Generated by Django 4.1.2 on 2023-01-20 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0041_postalcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='garage',
            name='postalCode',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parkingApp.postalcode'),
        ),
    ]
