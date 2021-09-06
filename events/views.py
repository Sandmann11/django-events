from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import Artist, Event, Venue
from .forms import EventForm, ArtistForm, VenueForm
from django.urls import reverse_lazy


now = datetime.now()

# def main(request):
#     return render(request, 'events/main.html', {})


# def home(request):
#     current_date = now.strftime('%d-%m-%Y')
#     current_time = now.strftime('%H:%M')
#     return render(request, 'events/home.html', {
#         'current_date': current_date,
#         'current_time': current_time,
#     })

class HomeView(TemplateView):
    template_name = 'events/home.html'


class EventList(ListView):
    model = Event
    template_name = 'events/event_list.html'
    ordering = ['start_date']


class EventDetails(DetailView):
    model = Event
    template_name = 'events/event_details.html'


class EventAdd(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_add.html'


class EventUpdate(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_update.html'


class EventDelete(DeleteView):
    model = Event
    template_name = 'events/event_delete.html'
    success_url = reverse_lazy('event_list')


class ArtistList(ListView):
    model = Artist
    template_name = 'events/artist_list.html'
    ordering = ['name']


class ArtistDetails(DetailView):
    model = Artist
    template_name = 'events/artist_details.html'


class ArtistAdd(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'events/artist_add.html'


class ArtistUpdate(UpdateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'events/artist_update.html'


class VenueList(ListView):
    model = Venue
    template_name = 'events/venue_list.html'
    ordering = ['name']


class VenueDetails(DetailView):
    model = Venue
    template_name = 'events/venue_details.html'


class VenueAdd(CreateView):
    model = Venue
    form_class = VenueForm
    template_name = 'events/venue_add.html'


class VenueUpdate(UpdateView):
    model = Venue
    form_class = VenueForm
    template_name = 'events/venue_update.html'

class ArchiveView(ListView):
    model = Event
    template_name = 'events/archive.html'
    ordering = ['-start_date']