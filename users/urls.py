from django.urls import path
from users.views import login,protected_view

urlpatterns = [
    path("login", login, name="login"),
    path("protected", protected_view, name="proctected")
]
