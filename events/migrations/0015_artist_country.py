# Generated by Django 3.2.6 on 2021-08-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20210811_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
