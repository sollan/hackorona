# Generated by Django 3.0.4 on 2020-03-21 19:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20200321_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='use_before',
            field=models.DateField(default=datetime.datetime(2020, 3, 28, 19, 27, 6, 617648, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='food',
            name='number',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='food',
            name='unit',
            field=models.CharField(blank=True, choices=[('UN', 'UN'), ('BG', 'BG'), ('BX', 'BX'), ('CN', 'CN'), ('CA', 'CA'), ('JR', 'JR'), ('PK', 'PK'), ('GR', 'GR'), ('KG', 'KG'), ('LT', 'LT')], max_length=2),
        ),
    ]