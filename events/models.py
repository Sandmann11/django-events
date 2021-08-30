from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from django.urls import reverse


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=75)
    address = models.CharField(max_length=200, blank=True)
    zip_code = zip_code = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100)
    province = models.CharField('State/Province', max_length=75, blank=True)
    country = models.CharField(max_length=100)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('venue_list')


class Artist(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='artist/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('artist_list')


class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):        
        return self.name

    def get_absolute_url(self):
        return reverse('category_list')
        


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    category = models.ForeignKey(Category, max_length=100, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, related_name='gigs', null=True, on_delete=models.CASCADE) 
    start_date = models.DateField('Start Date')
    start_time = models.TimeField('Start Time', blank=True, null=True)
    end_date = models.DateField('End Date')
    end_time = models.TimeField('End Time', blank=True, null=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(blank=True, null=True)
    lineup = models.ManyToManyField(Artist, related_name='gigs', blank=True)
    organizer = models.CharField(max_length=100, blank=True)
    website = models.URLField('Event Website', blank=True)
    phone = models.CharField('Contact Phone', max_length=25, null=True, blank=True)
    email = models.EmailField('Contact Email', blank=True)
    tickets = models.URLField('Buy Tickets URL', blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event_list')
