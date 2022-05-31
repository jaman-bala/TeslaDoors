from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, ListView
#
from .models import Product
from .forms import ProductForm


class Index(FormView, ListView):
    model = Product
    form_class = ProductForm
    context_object_name = 'informations'
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        img_obj = form.instance
        return super().form_valid(form)


class ReposView(ListView):
    model = Product
    context_object_name = 'informationsi'
    template_name = 'repos.html'
    success_url = reverse_lazy('repos')


