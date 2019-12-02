# Generated by Django 2.2.5 on 2019-12-02 16:29

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='asking_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
