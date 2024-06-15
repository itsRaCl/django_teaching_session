from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(["POST"])
def login(request):
    data = request.data
    username = data["username"]
    password = data["password"]

    user = authenticate(username=username, password=password)

    if (user):
        tokens = RefreshToken.for_user(user)

        return Response({"message" : "Verified!","access_token" : str(tokens.access_token) })
    else:
        return Response({"message" : "Invalid Username and password!"},status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
@permission_classes(( IsAuthenticated ,))
def protected_view(request):
    user = request.user
    
    if user.is_staff:
        return Response({"message" : "This is a protected view"})
    else:
        return Response({"message" : "You don't have access to this!"}, status=status.HTTP_401_UNAUTHORIZED)
