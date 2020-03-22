# Generated by Django 3.0.4 on 2020-03-21 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='food',
            name='last_name',
        ),
        migrations.AddField(
            model_name='food',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='food',
            name='status',
            field=models.CharField(choices=[('FR', 'Fresh'), ('EX', 'Expired')], default='FR', max_length=2),
        ),
        migrations.AddField(
            model_name='food',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
