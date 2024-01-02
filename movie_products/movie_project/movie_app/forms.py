from django import forms
from .models import Movies


class Movie_Form(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name', 'desc', 'year', 'genre', 'img']
