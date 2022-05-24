from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    paginate_by = 2
    template_name = 'index.html'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "products"
