# Generated by Django 4.1.2 on 2023-01-24 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0046_alter_garage_postalcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garage',
            name='postalCode',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parkingApp.postalcode'),
        ),
    ]