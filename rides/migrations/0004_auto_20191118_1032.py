# Generated by Django 2.2.5 on 2019-11-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0003_auto_20191118_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
