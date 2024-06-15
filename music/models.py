from django.db import models

# Create your models here.

class Album(models.Model):
    album_name = models.CharField(max_length = 100)
    band_name = models.CharField(max_length = 100)
    relase_date = models.DateField()


class Track(models.Model):
    album  = models.ForeignKey(to=Album, on_delete=models.CASCADE)
    track_name = models.CharField(max_length=100)
    description = models.TextField()
