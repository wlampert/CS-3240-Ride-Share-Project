# Generated by Django 2.2.5 on 2019-10-14 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0002_ride_seats_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='departure_date',
            field=models.DateField(),
        ),
    ]