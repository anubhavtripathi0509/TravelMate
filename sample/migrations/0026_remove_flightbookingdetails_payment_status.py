# Generated by Django 4.0.5 on 2024-12-25 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0025_flightbookingdetails_delete_bookingdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightbookingdetails',
            name='payment_status',
        ),
    ]
