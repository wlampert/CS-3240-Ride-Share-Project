# Generated by Django 2.2.5 on 2019-10-14 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0003_auto_20191014_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='departure_date',
            field=models.CharField(max_length=50),
        ),
    ]