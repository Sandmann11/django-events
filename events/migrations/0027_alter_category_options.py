# Generated by Django 3.2.6 on 2021-08-30 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0026_auto_20210819_0009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]