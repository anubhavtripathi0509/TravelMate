# Generated by Django 4.0.5 on 2024-12-25 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0027_busbookingdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busbookingdetails',
            name='booking_reference',
        ),
    ]