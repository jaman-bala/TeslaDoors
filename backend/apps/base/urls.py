from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<int:pk>', IndexDetail.as_view(), name='code_detail'),
    path('repos/', ReposView.as_view(), name='repos'),

]

