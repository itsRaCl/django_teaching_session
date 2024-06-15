from rest_framework import serializers
from music.models import Album, Track


# Albums, Tracks

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["album_name", "band_name", "relase_date"]

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"
