from django.contrib import admin
from .models import Artist, Category, Event, Venue


admin.site.register(Category)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country')
    list_filter = ('city', 'country')
    ordering = ('name',)
    search_fields = ('name', 'city', 'country')


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('country',)
    ordering = ('name',)
    search_fields = ('name', 'country')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'category', 'venue', 'start_date', 'end_date', 'description', 'lineup', 'image')
    list_display = ('name', 'start_date', 'category', 'venue')
    list_filter = ('start_date', 'category', 'venue')
    ordering = ('start_date',)
    search_fields = ('name', 'category', 'venue', 'lineup')