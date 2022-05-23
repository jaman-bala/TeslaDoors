
from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("products/", views.ProductListView.as_view(), name="product_list"),
]




