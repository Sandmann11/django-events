from django.contrib import admin
from .models import Artist, Category, Event, Venue


admin.site.register(Venue)
admin.site.register(Category)
admin.site.register(Artist)
admin.site.register(Event)
