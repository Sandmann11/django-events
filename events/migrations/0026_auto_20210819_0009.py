# Generated by Django 3.2.6 on 2021-08-18 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0025_alter_event_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='zip_code',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]