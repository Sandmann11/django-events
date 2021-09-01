from django.urls import path
from . import views
from .views import HomeView, EventList, EventDetails, EventAdd, EventUpdate, EventDelete, ArtistList, ArtistDetails, ArtistAdd, ArtistUpdate, VenueList, VenueDetails, VenueAdd, VenueUpdate


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('event_list/', EventList.as_view(), name='event_list'),
    path('event_details/<int:pk>/', EventDetails.as_view(), name='event_details'),
    path('event_add/', EventAdd.as_view(), name='event_add'),
    path('event_update/<int:pk>/', EventUpdate.as_view(), name='event_update'),
    path('event_delete/<int:pk>/', EventDelete.as_view(), name='event_delete'),
    
    path('artist_list/', ArtistList.as_view(), name='artist_list'),
    path('artist_details/<int:pk>/', ArtistDetails.as_view(), name='artist_details'),
    path('artist_add/', ArtistAdd.as_view(), name='artist_add'),
    path('artist_update/<int:pk>/', ArtistUpdate.as_view(), name='artist_update'),

    path('venue_list/', VenueList.as_view(), name='venue_list'),
    path('venue_details/<int:pk>/', VenueDetails.as_view(), name='venue_details'),
    path('venue_add/', VenueAdd.as_view(), name='venue_add'),
    path('venue_update/<int:pk>/', VenueUpdate.as_view(), name='venue_update'),
]
