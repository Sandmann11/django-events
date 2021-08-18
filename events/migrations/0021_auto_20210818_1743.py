# Generated by Django 3.2.6 on 2021-08-18 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_alter_event_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='lineup',
            field=models.ManyToManyField(blank=True, related_name='gigs', to='events.Artist'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(verbose_name='Start Date'),
        ),
    ]
