from django.contrib import admin
from primeapp.models import MainsectionMovie,MainsectionSeries

class MainsectionMovieAdmin(admin.ModelAdmin):
      list_display = ['title', 'genre','cover_image', 'video', 'imdb', 'year', 'time']
admin.site.register(MainsectionMovie,MainsectionMovieAdmin)

class MainsectionseriesAdmin(admin.ModelAdmin):
   
      list_display = ['title', 'genre','cover_image','video']
admin.site.register(MainsectionSeries,MainsectionseriesAdmin)