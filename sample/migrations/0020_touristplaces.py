# Generated by Django 3.2.1 on 2021-05-20 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0019_seasonsdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='TouristPlaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('cost', models.PositiveIntegerField()),
                ('time', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'touristplaces',
            },
        ),
    ]
