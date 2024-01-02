from django.contrib import admin
from . models import Genre
from . models import Most_Played
# Register your models here.

admin.site.register(Genre)
admin.site.register(Most_Played)