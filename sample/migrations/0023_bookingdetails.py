# Generated by Django 4.0.5 on 2024-12-22 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0022_distances'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_type', models.CharField(choices=[('Bus', 'Bus'), ('Flight', 'Flight')], max_length=10)),
                ('departure_date', models.DateField()),
                ('arrival_date', models.DateField()),
                ('fare', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_details', to='sample.user')),
            ],
        ),
    ]