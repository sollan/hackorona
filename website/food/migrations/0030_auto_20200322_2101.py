# Generated by Django 3.0.4 on 2020-03-22 21:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0029_auto_20200322_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='date_expiry',
            field=models.DateField(default=datetime.datetime(2020, 4, 21, 21, 1, 10, 472157, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='food',
            name='use_before',
            field=models.DateField(default=datetime.datetime(2020, 3, 29, 21, 1, 10, 472204, tzinfo=utc)),
        ),
    ]
