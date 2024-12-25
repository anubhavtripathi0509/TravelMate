# Generated by Django 3.2.1 on 2021-05-15 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0007_buses_bus_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buses',
            name='arrival_timeHours',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='buses',
            name='arrival_timeMinutes',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='buses',
            name='departure_timeHours',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='buses',
            name='departure_timeMinutes',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='flights',
            name='arrival_timeHours',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='flights',
            name='arrival_timeMinutes',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='flights',
            name='departure_timeHours',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='flights',
            name='departure_timeMinutes',
            field=models.CharField(max_length=2),
        ),
    ]