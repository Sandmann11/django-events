from django import forms
from .models import Venue, Artist, Category, Event


category_choices = Category.objects.all().values_list('name', 'name')
venue_choices = Venue.objects.all().values_list('name', 'name')
artist_choices = Artist.objects.all().values_list('name', 'name')


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'address', 'zip_code', 'city', 'province', 'country', 'website']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
        }


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'country', 'description', 'website', 'image']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '1000 characters max.'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Start URL with: https://'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'category', 'venue', 'start_date', 'end_date', 'lineup', 'description', 'image']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=category_choices, attrs={'class': 'form-control'}),
            'venue': forms.Select(choices=venue_choices, attrs={'class': 'form-control'}),
            'start_date': forms.SelectDateWidget(attrs={'class': 'form-control', 'placeholder': 'e.g.: 17.08.2021'}),
            'end_date': forms.SelectDateWidget(attrs={'class': 'form-control', 'placeholder': 'e.g.: 17.08.2021'}),
            'lineup': forms.SelectMultiple(choices=artist_choices, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '500 characters max.'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


