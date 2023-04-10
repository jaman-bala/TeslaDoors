from django.urls import path, include

from .views import sign_in, error

urlpatterns = [
    path("", sign_in, name="sign_in"),
    path("error/", error, name="error"),
]