# Generated by Django 4.0.3 on 2023-03-26 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='pickup_time',
            new_name='pickup',
        ),
    ]
