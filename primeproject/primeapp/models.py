from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
  
class MainsectionMovie(models.Model):
    GENRES = (
        (1, "Action and Adventure"),
        (2, "Comedy"),
        (3, "Drama"),
        (4, "Horror"),
        (5, "Romance"),
        (6, "Kids"),
        (7, "Mystery and Thrillers"), 
         (8, "sci-fi"), 
    )

    title = models.CharField(max_length=100)
    genre = models.IntegerField(choices=GENRES)
    description = models.TextField(max_length=700)
    cover_image = models.ImageField(upload_to='media/')
    video = models.FileField(upload_to='media/videos/')  # Example of using FileField for video uploads
    imdb = models.CharField(max_length=100)
    year = models.IntegerField()
    time = models.CharField(max_length=100)  # Renamed 'Time' to 'time' to follow Python naming conventions
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class MainsectionSeries(models.Model):
    GENRES = (
        (1, "Award-Winning Tv Shows"),
        (2, "Epic worlds"),
        (3, "Exciting Tv shows"),
        (4, "Marvel Tv shows"),
    )

    title = models.CharField(max_length=100)
    genre = models.IntegerField(choices=GENRES)
    description = models.TextField(max_length=1000)
    cover_image = models.ImageField(upload_to='media/')
    video = models.FileField(upload_to='media/videos/')  # Example of using FileField for video uploads
    season = models.CharField(max_length=100)  # Renamed 'Time' to 'time' to follow Python naming conventions
    ratings = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

