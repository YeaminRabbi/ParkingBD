# Generated by Django 4.1.2 on 2022-12-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0019_garage_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='other_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
