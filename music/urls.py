from operator import add
from django.urls import path
from music.views import ListAlbums, add_two_nums


urlpatterns = [
    path("", ListAlbums.as_view(), name="list_albums"),
    path("add", add_two_nums, name="add")
]
