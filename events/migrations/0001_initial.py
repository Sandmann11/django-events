# Generated by Django 3.2.6 on 2021-08-11 14:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True, verbose_name='Artist Website')),
                ('social_media', models.URLField(blank=True, verbose_name='Artist Social Media')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=15, verbose_name='Zip Code')),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True, verbose_name='Venue Website')),
                ('social_media', models.URLField(blank=True, verbose_name='Venue Social Media')),
                ('phone', models.CharField(blank=True, max_length=25, verbose_name='Contact Phone')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Contact Email')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('start_date', models.DateField(verbose_name='Event Start Date')),
                ('end_date', models.DateField(blank=True, verbose_name='Event End Date')),
                ('start_time', models.DateTimeField(blank=True, verbose_name='Event End Time')),
                ('description', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img')),
                ('organizer', models.CharField(blank=True, max_length=100)),
                ('website', models.URLField(blank=True, verbose_name='Event Website')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Event Contact Email')),
                ('social_media', models.URLField(blank=True, verbose_name='Event Social Media')),
                ('tickets', models.URLField(blank=True, verbose_name='Buy Tickets URL')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='events.category')),
                ('lineup', models.ManyToManyField(blank=True, to='events.Artist')),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.venue')),
            ],
        ),
    ]
