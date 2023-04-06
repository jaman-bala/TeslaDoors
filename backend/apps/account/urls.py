from django.urls import path, include

from .views import sign_in

urlpatterns = [
    path("", sign_in, name="sign_in"),
]