# Generated by Django 3.2.6 on 2021-09-05 22:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0028_auto_20210906_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
