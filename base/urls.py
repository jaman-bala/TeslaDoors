from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('repos/', ReposView.as_view(), name='repos'),

]

