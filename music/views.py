from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from music.models import Album
from music.serializers import AlbumSerializer

# Create your views here.


class ListAlbums(APIView):

    def get(self, request):
        albums = Album.objects.all()

        albums_data = AlbumSerializer(albums, many=True)

        return Response({"data": albums_data.data}, status=200)

    def post(self, request):
        data = request.data
        album_id = data["album_id"]
        album_name = data["album_name"]

        try:
            album = Album.objects.get(id=album_id)

            album.album_name = album_name
            album.save()
            album_s = AlbumSerializer(album)
            return Response(
                {"message": "Album updated!", "data": album_s.data},
                status=status.HTTP_200_OK,
            )
        except Album.DoesNotExist:
            return Response(
                {"message": "Album does not exist"}, status=status.HTTP_400_BAD_REQUEST
            )








@api_view(["GET"])
@permission_classes([IsAuthenticated])
def add_two_nums(request):
    data = request.data
    try: 
        num_1 = int(data["num_1"])
        num_2 = int(data["num_2"])
    except ValueError:
        return Response({"message" : "Please provied numbers"}, status=status.HTTP_400_BAD_REQUEST)


    result = num_1 + num_2

    return Response({"result" : result})


























