# Generated by Django 3.0.4 on 2020-03-21 19:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_auto_20200321_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='unit',
            field=models.CharField(choices=[('UN', 'unit(s)'), ('BG', 'bag(s)'), ('BX', 'box(es)'), ('CN', 'can(s)'), ('CA', 'carton(s)'), ('JR', 'jar(s)'), ('PK', 'package(s)'), ('GR', 'gram(s)'), ('KG', 'kilogram(s)'), ('LT', 'liter(s)')], default='UN', max_length=2),
        ),
        migrations.AlterField(
            model_name='food',
            name='use_before',
            field=models.DateField(default=datetime.datetime(2020, 3, 28, 19, 30, 35, 219793, tzinfo=utc)),
        ),
    ]